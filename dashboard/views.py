from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, UpdateProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages


@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    staff = User.objects.all()

    orders_count = Order.objects.all().count()
    products_count = Product.objects.all().count()
    staff_count = User.objects.all().count()
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
        "staff_count": staff_count,
        "products_count": products_count,
        "orders_count": orders_count,
        "orders": orders,
        "form": form,
        "products": products,
        


    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    staff = User.objects.all()
    staff_count = staff.count()
    items = Product.objects.all()
    product_count = items.count()
    orders = Order.objects.all()
    orders_count = orders.count()
    context = {
        'staff': staff,
        'staff_count': staff_count,
        'product_count': product_count,
        'orders_count': orders_count
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
    product_count = items.count()
    orders = Order.objects.all()
    orders_count = orders.count()
    staff = User.objects.all()
    staff_count = staff.count()
    form = ProductForm()

    if request.method == 'POST':
        form = form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product = form.cleaned_data.get('name')
            messages.success(request, f"{product} has been added")
            return redirect('dashboard-product')
    else:
        form = form = ProductForm()
    context = {
        'items': items,
        'form': form,
        'product_count': product_count,
        'orders_count': orders_count,
        'staff_count': staff_count
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url='user-login')
def order(request):
    items = Product.objects.all()
    product_count = items.count()
    orders = Order.objects.all()
    orders_count = orders.count()
    staff = User.objects.all()
    staff_count = staff.count()
    context = {
        'orders': orders,
        'product_count': product_count,
        'orders_count': orders_count,
        'staff_count': staff_count
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