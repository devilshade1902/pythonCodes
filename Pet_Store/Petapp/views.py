from django.shortcuts import get_object_or_404, render, redirect
from .models import Pet,Pet_Store,Pet_products,PetManager,Cart,Order,OrderItem
from django.http import HttpResponse,JsonResponse
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import PetUserForm
from django.contrib.auth.models import Permission
# from django.contrib.auth.decorators import permission
from django.contrib.auth.mixins import PermissionRequiredMixin ,LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.timezone import now
# Create your views here.

def homepage(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'about.html')

@login_required
def assign_permission_to_user(request):
    # user1
    pet_user = get_object_or_404(Pet_Store,username = "tiger1708")
    permission = Permission.objects.get(codename = 'can_add_pet')
    permission2 = Permission.objects.get(codename = 'can_update_pet')
    permission3 = Permission.objects.get(codename = 'can_delete_pet')
    permission4 = Permission.objects.get(codename = 'can_add_pet_products')
    permission5 = Permission.objects.get(codename = 'can_update_pet_products')
    permission6 = Permission.objects.get(codename = 'can_delete_pet_products')
    pet_user.user_permissions.add(permission,permission2,permission3,permission4,permission5,permission6)
    
    # user2
    pet_user2 = get_object_or_404(Pet_Store,username = "joel123")
    permission2 = Permission.objects.get(codename = 'can_update_pet')
    pet_user2.user_permissions.add(permission2)
    return HttpResponse("Permission added susscessfully")
    
    
def UserCreateView(request):
     if request.method == 'POST':
          pet_user_form = PetUserForm(request.POST)
          if pet_user_form.is_valid():
                pet_user_form.save()
                return redirect('petuser_list')
     else:
         pet_user_form = PetUserForm()
    
     return render(request,'user_create_form.html',{'pet_user_form':pet_user_form})

def searchView(request):
    query = request.GET.get('q')
    pet_manager = Pet.objects.search(query)
    return render(request,'search_results.html',{'query':query,'pet_manager':pet_manager})

class PetUserList(ListView):
    model = Pet_Store
    template_name = 'petuser_list.html'
    context_object_name = 'users'
    

class PetCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model=Pet
    template_name= 'pet_create_form.html'
    fields= ['name','breed','age','price','type','description', 'image']
    success_url= reverse_lazy('pet_list')
    
    permission_required = 'Petapp.can_add_pet'

class PetList(ListView):
    model= Pet
    template_name= 'pet_list.html'
    context_object_name= 'pets'


class PetDetailView(DetailView):
    model=Pet
    template_name='pet_detail_view.html'


class PetUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model=Pet
    template_name= 'pet_create_form.html'
    fields= ['name','breed','age','price','type','description', 'image']
    success_url= reverse_lazy('pet_list')
    
    permission_required = 'Petapp.can_update_pet'

class PetDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Pet
    template_name = 'pet_delete_view.html'
    success_url = reverse_lazy('pet_list')
    
    permission_required = 'Petapp.can_delete_pet'

class ProductCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model=Pet_products
    template_name= 'product_create_view.html'
    fields= ['product_name','category','price','quantity_in_stock','description', 'image']
    success_url= reverse_lazy('product_list')
    
    permission_required = 'Petapp.can_add_pet_products'

class ProductList(ListView):
    model= Pet_products
    template_name= 'productlist_view.html'
    context_object_name= 'pet_products'
    
class ProductDetailView(DetailView):
    model = Pet_products
    template_name = 'product_detail_view.html'
    context_object_name = 'product'

class ProductDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Pet_products
    template_name = 'product_delete_view.html'
    success_url = reverse_lazy('product_list')
    
    permission_required = 'Petapp.can_delete_pet_products'
    
    
class ProductUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model=Pet_products
    template_name= 'product_create_view.html'
    fields= ['product_name','category','price','quantity_in_stock','description', 'image']
    success_url= reverse_lazy('product_list')
    
    permission_required = 'Petapp.can_update_pet_products'
    


class AddToCartView(View):
    def post(self, request):
        if request.user.is_authenticated:
            pet_id = request.POST.get('pet_id')
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))

            pet = None
            product = None

            if pet_id:
                pet = get_object_or_404(Pet, id=pet_id)

            if product_id:
                product = get_object_or_404(Pet_products, id=product_id)

            if not pet and not product:
                return JsonResponse({'error': 'No pet or product added to cart'}, status=400)

            cart_item, created = Cart.objects.get_or_create(
                customer_id = request.user,
                pet_id = pet,
                product_id = product,
                defaults = {'quantity': quantity, 'date_added': now()}
            )

            if not created:
                cart_item.quantity += 1
                cart_item.save()

            return redirect('view_cart')
        return JsonResponse({'error': 'You need to log in first..!'}, status=403)

class CartView(ListView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cart.objects.filter(customer_id=self.request.user)
        return Cart.objects.none()
    
class RemoveFromCartView(View):
    def post(self, request, cart_id):
        if request.user.is_authenticated:
            cart_item = get_object_or_404(Cart, id=cart_id, customer_id=request.user)
            cart_item.delete()
            return redirect('view_cart')
    

class CreateOrderView(View):
    def post(self, request):
        if request.user.is_authenticated:
            cart_items = Cart.objects.filter(customer_id=request.user)
            if not cart_items:
                return JsonResponse({'error': 'Cart is empty'})
            
            total_amount = 0
            for item in cart_items:
                if item.pet_id:
                    total_amount += item.pet_id.price * item.quantity
                elif item.product_id:
                    total_amount += item.product_id.price * item.quantity
            
            order = Order.objects.create(
                user_id = request.user,
                order_date = now(),
                total_amount = total_amount    
            )

            for item in cart_items:
                if item.pet_id:
                    OrderItem.objects.create(
                        order_id=order,
                        pet_id=item.pet_id,
                        quantity=item.quantity,
                        price=item.pet_id.price * item.quantity
                    )
                elif item.product_id:
                    OrderItem.objects.create(
                        order_id=order,
                        product_id=item.product_id,
                        quantity=item.quantity,
                        price=item.product_id.price * item.quantity
                    )
            
            cart_items.delete()

            return redirect('order_summary', order_id=order.id)
        return JsonResponse({'error': 'You need to log in first'}, status=403)


class OrderSummaryView(View):
    template_name = 'order_summary.html'

    def get(self, request, order_id):
        if request.user.is_authenticated:
            # Fetch the order
            order = get_object_or_404(Order, id=order_id, user_id=request.user)
            
            # Fetch the related order items
            order_items = OrderItem.objects.filter(order_id=order)
            
            # Prepare context data for rendering
            context = {
                'order': order,
                'order_items': order_items,
            }
            return render(request, self.template_name, context)
        else:
            return JsonResponse({'error': 'You need to log in first.'}, status=403)
        
