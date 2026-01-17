from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.add_employee),
    path('employee/<int:id>/', views.get_employeeby_id),
    path('employee/active/', views.get_active_employee),
    path('employee/update/<int:id>/', views.update_employee),
    path('employee/delete/<int:id>/', views.delete_employee),
]
