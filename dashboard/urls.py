from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>', views.delete_product, name='delete-product'),
    path('order/', views.order, name='dashboard-order'),
]