from django.urls import path
from .views import EmployeeList
from .views import EmployeeCreateView,EmployeeDetailView,EmployeeUpdateView,EmployeeDeleteView

urlpatterns = [
    path('emp_list',EmployeeList.as_view(),name='emp_list'),
    path('create_emp',EmployeeCreateView.as_view(), name = 'create_emp'),
    path('<int:pk>/',EmployeeDetailView.as_view(), name='emp_detail_view'),
    path('update_emp/<int:pk>/',EmployeeUpdateView.as_view(),name = 'update_view'),
    path('delete_view/<int:pk>/',EmployeeDeleteView.as_view(),name = 'delete_view')
]