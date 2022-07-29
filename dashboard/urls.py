from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/', views.delete_product, name='delete-product'),
    path('product/update/<int:pk>/', views.update_product, name='update-product'),
    path('order/', views.order, name='dashboard-order'),
]