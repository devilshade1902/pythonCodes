from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView 
from .views import CreateOrderView,OrderSummaryView ,RemoveFromCartView,CartView,AddToCartView,aboutus,searchView,ProductUpdateView,ProductDeleteView,ProductList,ProductCreateView,ProductDetailView,PetList,PetCreateView,PetDetailView,PetUpdateView,PetDeleteView,PetUserList,homepage, UserCreateView

urlpatterns=[
        path('home/',homepage,name = 'home'),
        path('aboutus/',aboutus,name = 'aboutus'),
        path('create_user/',UserCreateView,name = 'create_user'),
        path('petuser_list',PetUserList.as_view(),name = 'petuser_list'),
        path('pet_list/',PetList.as_view(),name='pet_list'),
        path('create_pet/',PetCreateView.as_view(),name='create_pet'),
        path('<int:pk>/',PetDetailView.as_view(),name='pet_detail_view'),
        path('update_pet/<int:pk>/',PetUpdateView.as_view(),name = 'update_view'),
        path('delete_pet/<int:pk>/',PetDeleteView.as_view(),name = 'delete_view'),
        path('product_list/',ProductList.as_view(),name='product_list'),
        path('create_product/',ProductCreateView.as_view(),name='create_product'),
        path('products/<int:pk>/',ProductDetailView.as_view(),name='product_detail_view'),
        path('delete_product/<int:pk>/',ProductDeleteView.as_view(),name ='product_delete'),
        path('update_product/<int:pk>/',ProductUpdateView.as_view(),name = 'update_product'),
        path('login/',LoginView.as_view(template_name = 'login.html'),name = 'login'),
        path('logout/',LogoutView.as_view(next_page = 'login'),name = 'logout'),
        path('search/',searchView,name = 'search'),
        path('add_to_cart/',AddToCartView.as_view(), name="add_to_cart"),
        path('remove_from_cart/<int:cart_id>/', RemoveFromCartView.as_view(), name="remove_from_cart"),
        path('view_cart/', CartView.as_view(), name="view_cart"),
        path('create_order/', CreateOrderView.as_view(), name="create_order"),
        path('order_summary/<int:order_id>/', OrderSummaryView.as_view(), name="order_summary"),
 ]