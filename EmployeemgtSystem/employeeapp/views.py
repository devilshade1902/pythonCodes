from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def emp_list(request):
    employees = Employee.objects.all()
    return render(request,'emp_list.html',{'employess':employees})

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'emp_create_form.html'
    fields = ['empno','ename','email']
    success_url = reverse_lazy ('emp_list')



class EmployeeList(ListView):
    model= Employee
    template_name = 'emp_list.html' 
    context_object_name = 'employees'


class EmployeeDetailView(DetailView):
    model= Employee
    template_name = 'emp_detail_view.html'


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'emp_create_form.html'
    fields = ['empno','ename','email']
    success_url = reverse_lazy ('emp_list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'emp_delete_view.html'
    success_url = reverse_lazy('emp_list')