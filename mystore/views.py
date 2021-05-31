from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from web_pizza.models import Topping, Pizza, Soda, Side, Product, Customer, Order, Category
from .forms import CustomerForm, OrderForm, SideForm, SodaForm, PizzaForm, ToppingForm


def mystore(request):
    # category = None
    # categories = Category.objects.all()
    # products = Product.objects.all()
    # context = {'cartegories': categories, 'products': products}
    return render(request, 'mystore.html', {'user': 'Admin'})

def lookup_products(request):
    return render(request, 'productslookup.html')

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
        return render(request, 'ordercreate.html', {'form': form})
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
    context = {}
    context["orders"] = Order.objects.all()
    return render(request, 'orderlookup.html', context)

def create_customer(request):
    form = CustomerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Customer Created Successfully'))
        return render(request, 'customercreate.html', {'form': form})
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
    context = {}
    context["customers"] = Customer.objects.all()
    return render(request, 'customerlookup.html', context)

def toppingyeah(request, id):
    context = {}
    context["dataset"] = Topping.objects.all()
    obj = get_object_or_404(Side, id=id)
    form = ToppingForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context["form"] = form
    return render(request, "toppingyeah.html", context)

    # if request.method == 'POST':
    #     topping_name = request.POST['topping_name']
    #
    # else:
    #    messages.info({topping_name}, ' Added Successfully.')
    #    return render(request, 'results.html', {'result': messages}, {'user': 'Admin'})

def pizzayeah(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas':pizzas}
    return render(request, "pizzayeah.html", context)

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
    context = {'sodas': sodas}
    return render(request, "sodayeah.html", context)

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
    context = {'sides': sides}
    return render(request, "sideyeah.html", context)

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

