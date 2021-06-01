from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from web_pizza.models import Topping, Pizza, Soda, Side, Product, Customer, Order, Category
from .forms import CustomerForm, OrderForm, SideForm, SodaForm, PizzaForm, ToppingForm


def mystore(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='3').count()
    pending = orders.filter(status='0').count()

    return render(request, 'mystore.html', {'orders': orders, 'customers': customers, 'total_customers': total_customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending})

def lookup_products(request):
    products = Product.objects.all()
    pizzas = Pizza.objects.all()
    sodas = Soda.objects.all()
    sides = Side.objects.all()
    return render(request, 'productslookup.html', {'products': products, 'pizzas': pizzas, 'sodas': sodas, 'sides': sides})

def results(request):
    context = {}
    context["dataset"] = Topping.objects.all()
    return render(request, 'results.html', context)

def create_order(request):
    form = OrderForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('There was an error creating the Order. Please try again...'))
            return render(request, 'ordercreate.html', {'form': form})
        messages.success(request, ('Order Created Successfully'))
        orders = Order.objects.all()
        return render(request, 'orderlookup.html', {'orders': orders})
    else:
        return render(request, 'ordercreate.html', {'form': form})

def update_order(request, orderID):
    orderID = (orderID)
    try:
        order_select = Order.objects.get(id=orderID)
    except Order.DoesNotExist:
        return render(request, 'mystore.html', {'user': 'Admin'})
    order_form = OrderForm(request.POST or None, instance = order_select)
    if order_form.is_valid():
       order_form.save()
       return render(request, 'mystore.html', {'user': 'Admin'})
    return render(request, 'orderupdate.html', {'order_form': order_form})

def delete_order(request, orderID):
    context ={}
    obj = get_object_or_404(Order, orderID=orderID)
    if request.method == "POST":
        obj.delete()
        messages.success(request, ('Order Deleted Successfully'))
        return render(request, 'mystore.html', {'user': 'Admin'})
    else:
        return render(request, 'orderdelete.html', context)

def lookup_order(request):
    orders = Order.objects.all()
    return render(request, 'orderlookup.html', {'orders': orders})

def create_customer(request):
    form = CustomerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Customer Created Successfully'))
        context = {}
        context["customers"] = Customer.objects.all()
        return render(request, 'customerlookup.html', context)
    else:
        return render(request, 'customercreate.html', {'form': form})

def update_customer(request, customerID):
    customerID = (customerID)
    try:
        customer_select = Customer.objects.get(id=customerID)
    except Customer.DoesNotExist:
        return render(request, 'mystore.html', {'user': 'Admin'})
    customer_form = CustomerForm(request.POST or None, instance=customer_select)
    if customer_form.is_valid():
        customer_form.save()
        return render(request, 'mystore.html', {'user': 'Admin'})
    return render(request, 'customerupdate.html', {'customer_form': customer_form})

def delete_customer(request, customerID):
    context = {}
    obj = get_object_or_404(Customer, customerID=customerID)
    if request.method == "POST":
        obj.delete()
        messages.success(request, ('Customer Deleted Successfully'))
        return render(request, 'mystore.html', {'user': 'Admin'})
    else:
        return render(request, 'customerdelete.html', context)

def lookup_customer(request):
    customers = Customer.objects.all()
    return render(request, 'customerlookup.html', {'customers': customers})

def toppingyeah(request):
    toppings = Topping.objects.all()
    form = ToppingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Topping Created Successfully'))
        toppings = Topping.objects.all()
        return render(request, "toppingyeah.html", {'toppings': toppings})
    else:
        return render(request, "toppingyeah.html", {'toppings': toppings})

    # if request.method == 'POST':
    #     topping_name = request.POST['topping_name']
    #
    # else:
    #    messages.info({topping_name}, ' Added Successfully.')
    #    return render(request, 'results.html', {'result': messages}, {'user': 'Admin'})

def pizzayeah(request):
    pizzas = Pizza.objects.all()
    form = PizzaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Pizza Created Successfully'))
        pizzas = Pizza.objects.all()
        return render(request, "pizzayeah.html", {'pizzas': pizzas})
    else:
        return render(request, "pizzayeah.html", {'pizzas': pizzas})

    '''context = {}
    obj = get_object_or_404(Side, id=id)
    form = PizzaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context["form"] = form
    return render(request, "pizzayeah.html", context)'''

    # if request.method == 'POST':
    #     pizza_name = request.POST['pizza_name']
    #     pizza_size = request.POST['pizza_size']
    #     pizza_price = request.POST['pizza_price']
    #
    #     if pizza_size=='Small' or 'Medium' or 'Large':
    #         messages.info(request, 'Pizza Size needs to be either Small, Medium, or Large')
    #         return redirect('mystore')
    #     else:
    #         messages.info(request, {pizza_name}, ',', {pizza_size}, ', and', {pizza_price}, ' Added Successfully.')
    #         return render(request, 'results.html', {'result': messages}, {'user': 'Admin'})

def sodayeah(request):
    sodas = Soda.objects.all()
    form = SodaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Soda Created Successfully'))
        sodas = Soda.objects.all()
        return render(request, "sodayeah.html", {'sodas': sodas})
    else:
        return render(request, "sodayeah.html", {'sodas': sodas})

    # context = {}
    # obj = get_object_or_404(Side, id=id)
    # form = SodaForm(request.POST or None, instance=obj)
    # if form.is_valid():
    #     form.save()
    #     return HttpResponseRedirect("/" + id)
    # context["form"] = form
    # return render(request, "sodayeah.html", context)

    # if request.method == 'POST':
    #     soda_name = request.POST['soda_name']
    #     soda_size = request.POST['soda_size']
    #     soda_price = request.POST['soda_price']
    #
    #     if soda_size == '12 Oz' or '2 Litter':
    #         messages.info(request, 'Soda Size needs to be either 12 Oz or 2 Litter')
    #         return redirect('mystore')
    #
    #     else:
    #         messages.info({soda_name}, ',', {soda_size}, ', and', {soda_price}, ' Added Successfully.')
    #         return render(request, 'results.html', {'result': messages}, {'user': 'Admin'})

def sideyeah(request):
    sides = Side.objects.all()
    form = SideForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Side Created Successfully'))
        sides = Side.objects.all()
        return render(request, "sideyeah.html", {'sides': sides})
    else:
        return render(request, "sideyeah.html", {'sides': sides})



    '''context = {}
    obj = get_object_or_404(Side, id=id)
    form = SideForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context["form"] = form
    return render(request, "sideyeah.html", context)'''

    # if request.method == 'POST':
    #     side_name = request.POST['side_name']
    #     side_price = request.POST['side_price']
    #
    # else:
    #     messages.info(request, {side_name}, ' and', {side_price}, ' Added Successfully.')
    #     return render(request, 'results.html', {'result': messages}, context)

