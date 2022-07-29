from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, UpdateProductForm, OrderForm
from django.contrib.auth.models import User


@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()

    context = {
        "orders": orders,
        "form": form

    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    staff = User.objects.all()
    context = {
        'staff': staff
    }
    return render(request, 'dashboard/staff.html', context)

def staff_detail(request, pk):
    worker = User.objects.get(id=pk)
    context = {
        'worker': worker
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = form = ProductForm()
    context = {
        'items': items,
        'form': form
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'dashboard/order.html', context)


def delete_product(request, pk):
    item = Product.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect("dashboard-product")
    return render(request, 'dashboard/product_delete.html')


def update_product(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'dashboard/update_product.html', {'form': form})