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
    delivered = orders.filter(status='3').count()
    pending = orders.filter(status='0').count()

    return render(request, 'mystore.html', {'orders': orders, 'customers': customers, 'total_customers': total_customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending})

def lookup_products(request):
    products = Product.objects.all()
    pizzas = Pizza.objects.all()
    sodas = Soda.objects.all()
    sides = Side.objects.all()
    return render(request, 'productslookup.html', {'products': products, 'pizzas': pizzas, 'sodas': sodas, 'sides': sides})

def delete_product(request, pk):
    context = {}
    obj = get_object_or_404(Product, id=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, ('Product Deleted Successfully'))
        return render(request, 'mystore.html')
    else:
        return render(request, 'productdelete.html', context)

def update_product(request, pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    context = {'product': product, 'products': products}
    if request.method == "POST":
        form = ProductForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            if form.isnot_valid():
                messages.success(request, ('There was an error updating the Order. Please try again...'))
                return render(request, 'productupdate.html', context)
            messages.success(request, ('Product Updated Successfully'))
            return render(request, 'mystore.html')
    return render(request, 'productupdate.html', context)

def create_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            if form.isnot_valid():
                messages.success(request, ('There was an error creating the Order. Please try again...'))
                return render(request, 'ordercreate.html', context)
            messages.success(request, ('Order Created Successfully'))
            return render(request, 'mystore.html')
    context = {'form': form}
    return render(request, 'ordercreate.html', context)

    '''form = OrderForm(request.POST or None)
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
        return render(request, 'ordercreate.html', {'form': form})'''

    # form = OrderForm(request.POST or None)
    # orders = Order.objects.all()
    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         messages.success(request, ('There was an error creating the Order. Please try again...'))
    #         return render(request, 'ordercreate.html', {'form': form, 'orders':orders})
    #     messages.success(request, ('Order Created Successfully'))
    #     orders = Order.objects.all()
    #     return render(request, 'orderlookup.html', {'orders': orders})
    #     return render(request, 'ordercreate.html', {'form': form, 'orders':orders})
    # else:
    #     return render(request, 'ordercreate.html', {'form': form, 'orders':orders})

def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {'form': form}
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            if form.isnot_valid():
                messages.success(request, ('There was an error updating the Order. Please try again...'))
                return render(request, 'orderupdate.html', context)
            messages.success(request, ('Order Updated Successfully'))
            return render(request, 'mystore.html')
    return render(request, 'orderupdate.html', context)

    '''try:
        order_select = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return render(request, 'mystore.html')
    order_form = OrderForm(request.POST or None, instance = order_select)
    if order_form.is_valid():
       order_form.save()
       return render(request, 'mystore.html')'''


    # orderID = (orderID)
    # orders = Order.objects.all()
    # try:
    #     order_select = Order.objects.get(id=orderID)
    # except Order.DoesNotExist:
    #     return render(request, 'mystore.html', {'user': 'Admin', 'orders':orders})
    # order_form = OrderForm(request.POST or None, instance = order_select)
    # if order_form.is_valid():
    #    order_form.save()
    #    return render(request, 'mystore.html', {'user': 'Admin'})
    # return render(request, 'orderupdate.html', {'order_form': order_form, 'orders':orders})

def delete_order(request, pk):
    context = {}
    obj = get_object_or_404(Order, id=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, ('Order Deleted Successfully'))
        return render(request, 'mystore.html')
    else:
        return render(request, 'orderdelete.html', context)


    # context ={}
    # orders = Order.objects.all()
    # obj = get_object_or_404(Order, orderID=orderID)
    # if request.method == "POST":
    #     obj.delete()
    #     messages.success(request, ('Order Deleted Successfully'))
    #     return render(request, 'mystore.html', {'orders':orders})
    # else:
    #     return render(request, 'orderdelete.html', context, {'orders':orders})

def lookup_order(request):
    orders = Order.objects.all()
    return render(request, 'orderlookup.html', {'orders': orders})

    # context = {}
    # orders = Order.objects.all()
    # context["orders"] = Order.objects.all()
    # return render(request, 'orderlookup.html', context, {'orders':orders})


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


    # form = CustomerForm(request.POST or None)
    # orders = Order.objects.all()
    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()
    #     messages.success(request, ('Customer Created Successfully'))
    #
    #     context = {}
    #     context["customers"] = Customer.objects.all()
    #     return render(request, 'customerlookup.html', context)
    #
    #     return render(request, 'customercreate.html', {'form': form, 'orders':orders})
    #
    # else:
    #     return render(request, 'customercreate.html', {'form': form, 'orders':orders})

def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customers = Customer.objects.all()
    orders = Order.objects.all()
    customerorders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'customers': customers, 'orders': orders, 'customerorders': customerorders,
               'order_count': order_count}
    return render(request, 'customerupdate.html', context)

    '''try:
        customer_select = Customer.objects.get(id=customerID)
    except Customer.DoesNotExist:
        return render(request, 'mystore.html')
    customer_form = CustomerForm(request.POST or None, instance=customer_select)
    if customer_form.is_valid():
        customer_form.save()
        return render(request, 'mystore.html')'''


    # customerID = (customerID)
    # orders = Order.objects.all()
    # try:
    #     customer_select = Customer.objects.get(id=customerID)
    # except Customer.DoesNotExist:
    #     return render(request, 'mystore.html', {'user': 'Admin'})
    # customer_form = CustomerForm(request.POST or None, instance=customer_select)
    # if customer_form.is_valid():
    #     customer_form.save()
    #     return render(request, 'mystore.html', {'user': 'Admin'})
    # return render(request, 'customerupdate.html', {'customer_form': customer_form, 'orders':orders})

def delete_customer(request, pk):
    context = {}
    obj = get_object_or_404(Customer, id=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, ('Customer Deleted Successfully'))
        return render(request, 'mystore.html')
    else:
        return render(request, 'customerdelete.html', context)

    # context = {}
    # orders = Order.objects.all()
    # obj = get_object_or_404(Customer, customerID=customerID)
    # if request.method == "POST":
    #     obj.delete()
    #     messages.success(request, ('Customer Deleted Successfully'))
    #     return render(request, 'mystore.html', {'user': 'Admin'})
    # else:
    #     return render(request, 'customerdelete.html', context, {'orders':orders})

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
        return render(request, "toppingyeah.html", {'toppings': toppings, 'form': form})
    else:
        return render(request, "toppingyeah.html", {'toppings': toppings, 'form': form})

'''def toppingyeah(request, id):
    context = {}
    context["dataset"] = Topping.objects.all()
    orders = Order.objects.all()
    obj = get_object_or_404(Side, id=id)
    form = ToppingForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context["form"] = form
    return render(request, "toppingyeah.html", context, {'orders':orders})'''

def pizzayeah(request):
    pizzas = Pizza.objects.all()
    form = PizzaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Pizza Created Successfully'))
        pizzas = Pizza.objects.all()
        return render(request, "pizzayeah.html", {'pizzas': pizzas, 'form': form})
    else:
        return render(request, "pizzayeah.html", {'pizzas': pizzas, 'form': form})

    '''context = {}
    obj = get_object_or_404(Side, id=id)
    form = PizzaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context["form"] = form
    return render(request, "pizzayeah.html", context)'''

def sodayeah(request):
    sodas = Soda.objects.all()
    form = SodaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Soda Created Successfully'))
        sodas = Soda.objects.all()
        return render(request, "sodayeah.html", {'sodas': sodas, 'form': form})
    else:
        return render(request, "sodayeah.html", {'sodas': sodas, 'form': form})

    '''context = {}
    obj = get_object_or_404(Side, id=id)
    form = SodaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context["form"] = form
    return render(request, "sodayeah.html", context)'''

def sideyeah(request):
    sides = Side.objects.all()
    form = SideForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request, ('Side Created Successfully'))
        sides = Side.objects.all()
        return render(request, "sideyeah.html", {'sides': sides, 'form': form})
    else:
        return render(request, "sideyeah.html", {'sides': sides, 'form': form})

    '''context = {}
    obj = get_object_or_404(Side, id=id)
    form = SideForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context["form"] = form
    return render(request, "sideyeah.html", context)'''
