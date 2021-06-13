from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from web_pizza.models import Topping, Pizza, Soda, Side, Product, Customer, Order, Category
from .forms import CustomerForm, OrderForm, SideForm, SodaForm, PizzaForm, ToppingForm
from databaseController import DatabaseController

def mystore(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    received = orders.filter(status='Order Received').count()
    baking = orders.filter(status='Baking').count()
    ontheway = orders.filter(status='On The Way').count()

    return render(request, 'mystore.html', {'orders': orders, 'customers': customers, 'total_customers': total_customers,
                                            'total_orders': total_orders, 'delivered': delivered, 'received': received,
                                            'baking': baking, 'ontheway': ontheway})

def lookup_products(request):
    products = Product.objects.all()
    pizzas = Pizza.objects.all()
    sodas = Soda.objects.all()
    sides = Side.objects.all()
    return render(request, 'productslookup.html', {'products': products, 'pizzas': pizzas, 'sodas': sodas, 'sides': sides})

def delete_soda(request, pk):
    context = {}
    obj = get_object_or_404(Soda, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, ('Soda Deleted Successfully'))
        return redirect('mystore:mystore')
    return render(request, 'productdelete.html', context)

def delete_side(request, pk):
    context = {}
    obj = get_object_or_404(Side, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, ('Side Deleted Successfully'))
        return redirect('mystore:mystore')
    return render(request, 'productdelete.html', context)

def delete_pizza(request, pk):
    context = {}
    obj = get_object_or_404(Pizza, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, ('Pizza Deleted Successfully'))
        return redirect('mystore:mystore')
    return render(request, 'productdelete.html', context)

def delete_topping(request, pk):
    context = {}
    obj = get_object_or_404(Topping, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, ('Topping Deleted Successfully'))
        return redirect('mystore:mystore')
    return render(request, 'productdelete.html', context)

def update_soda(request, pk):
    soda = Soda.objects.get(pk=pk)
    form = SodaForm(instance=soda)
    context = {'form': form}
    if request.method == "POST":
        form = SodaForm(request.POST, instance=soda)
        if form.is_valid():
            form.save()
            messages.success(request, ('Soda Updated Successfully'))
            return redirect('mystore:mystore')
    return render(request, 'productupdate.html', context)

def update_side(request, pk):
    side = Side.objects.get(pk=pk)
    form = SideForm(instance=side)
    context = {'form': form}
    if request.method == "POST":
        form = SideForm(request.POST, instance=side)
        if form.is_valid():
            form.save()
            messages.success(request, ('Side Updated Successfully'))
            return redirect('mystore:mystore')
    return render(request, 'productupdate.html', context)

def update_pizza(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    context = {'form': form}
    if request.method == "POST":
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            messages.success(request, ('Pizza Updated Successfully'))
            return redirect('mystore:mystore')
    return render(request, 'productupdate.html', context)

def update_topping(request, pk):
    topping = Topping.objects.get(pk=pk)
    form = ToppingForm(instance=topping)
    context = {'form': form}
    if request.method == "POST":
        form = ToppingForm(request.POST, instance=topping)
        if form.is_valid():
            form.save()
            messages.success(request, ('Topping Updated Successfully'))
            return redirect('mystore:mystore')
    return render(request, 'productupdate.html', context)

def create_order(request):
    orders = Order.objects.all()
    form = OrderForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Order Created Successfully'))
        orders = Order.objects.all()
        return render(request, "ordersyeah.html", {'orders': orders, 'form': form})
    return render(request, "ordersyeah.html", {'orders': orders, 'form': form})

def update_order(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    context = {'form': form}
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, ('Order Updated Successfully'))
            return redirect('mystore:mystore')
    return render(request, 'orderupdate.html', context)

def delete_order(request, orderID):
    context = {}
    obj = get_object_or_404(Order, orderID=orderID)
    if request.method == "POST":
        obj.delete()
        messages.success(request, ('Order Deleted Successfully'))
        return redirect('mystore:mystore')
    else:
        return render(request, 'orderdelete.html', context)

def lookup_order(request):
    orders = Order.objects.all()
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Order Created Successfully'))
            return redirect('mystore:mystore')
    context = {'form': form, 'orders': orders}
    return render(request, 'ordersyeah.html', context)

def create_customer(request):
    customers = Customer.objects.all()
    form = CustomerForm(request.POST or None)
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, ('Customer Created Successfully'))
        return redirect('mystore:mystore')
    return render(request, "customercreate.html", {'customers': customers, 'form': form})

def delete_customer(request, pk):
    context = {}
    obj = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, ('Customer Deleted Successfully'))
        return redirect('mystore:mystore')
    else:
        return render(request, 'customerdelete.html', context)

def lookup_customer(request):
    customers = Customer.objects.all()
    form = CustomerForm(request.POST or None)
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, ('Customer Created Successfully'))
        return redirect('mystore:mystore')
    context = {'customers': customers, 'form': form}
    return render(request, "customersyeah.html", context)

def update_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    form = CustomerForm(instance=customer)
    context = {'form': form}
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, ('Customer Updated Successfully'))
            return redirect('mystore:mystore')
    return render(request, 'customerupdate.html', context)

def toppingyeah(request):
    toppings = Topping.objects.all()
    form = ToppingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Topping Created Successfully'))
        toppings = Topping.objects.all()
        return render(request, "toppingyeah.html", {'toppings': toppings, 'form': form})
    return render(request, "toppingyeah.html", {'toppings': toppings, 'form': form})

def pizzayeah(request):
    pizzas = Pizza.objects.all()
    form = PizzaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Pizza Created Successfully'))
        pizzas = Pizza.objects.all()
        return render(request, "pizzayeah.html", {'pizzas': pizzas, 'form': form})
    return render(request, "pizzayeah.html", {'pizzas': pizzas, 'form': form})

def sodayeah(request):
    sodas = Soda.objects.all()
    form = SodaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Soda Created Successfully'))
        sodas = Soda.objects.all()
        return render(request, "sodayeah.html", {'sodas': sodas, 'form': form})
    return render(request, "sodayeah.html", {'sodas': sodas, 'form': form})

def sideyeah(request):
    sides = Side.objects.all()
    form = SideForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Side Created Successfully'))
        sides = Side.objects.all()
        return render(request, "sideyeah.html", {'sides': sides, 'form': form})
    return render(request, "sideyeah.html", {'sides': sides, 'form': form})