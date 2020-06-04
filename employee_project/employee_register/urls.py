from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee_form, name='employee_form'),
    path('<int:employee_id>', views.employee_form, name='employee_update'),
    path('delete/<int:employee_id>', views.employee_delete, name='employee_delete'),
    path('list/', views.employee_list, name='employee_list')
]
