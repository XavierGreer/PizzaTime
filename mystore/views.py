from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from web_pizza.models import Topping, Pizza, Soda, Side, Product, Customer, Order
from .forms import CustomerForm, OrderForm


def mystore(request):
    return render(request, 'mystore.html', {'user': 'Admin'})

def results(request):
    return render(request, 'results.html', {'user': 'Admin'})

# def results(request):
#     t_list = Topping.objects.get(all(object))
#     context = {
#         'object': t_list
#     }
#     return render(request, 'results.html', context)

# def results(request):
#     try:
#         toppings = Topping.objects.get().orderby('name')
#     except Topping.DoesNotExist:
#         raise Http404('Topping does not exist')
#     context = {
#         'toppings': toppings
#     }
#     return render(request, 'results.html', {'user': 'Admin'}, context)

def edit_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'orderlookup.html', context)

# def create_order(request):
#     form = OrderForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = OrderForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'orderlookup.html', context)
#
# def delete_order(request):
#     form = OrderForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = OrderForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'orderlookup.html', context)

def edit_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerForm()
    context = {
        'form': form
    }
    return render(request, 'customerlookup.html', context)

# def add_customer(request):
#     form = CustomerForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = CustomerForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'customerlookup.html', context)

# def delete_customer(request):
#     form = CustomerForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = CustomerForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'customerlookup.html', context)

# def add_topping(request):
#
#     toppings_list = Topping.objects.all()
#     output = ', '.join([t.topping_name for t in toppings_list])
#     return render(request, 'results.html', {'user': 'Admin'}, {'return_t': output})

# def add_topping(request):
#
#     if request.method == 'POST':
#         topping_name = request.POST['topping_name']
#
# else:
#    messages.info({topping_name}, ' Added Successfully.')
#    return render(request, 'results.html', {'result': messages}, {'user': 'Admin'})

# def add_pizza(request):
#
#     if request.method == 'POST':
#         pizza_name = request.POST['pizza_name']
#         pizza_size = request.POST['pizza_size']
#         pizza_price = request.POST['pizza_price']
#
#         if pizza_size=='Small' or 'Medium' or 'Large':
#             messages.info(request, 'Pizza Size needs to be either Small, Medium, or Large')
#             return redirect('mystore')
#         else:
#             messages.info(request, {pizza_name}, ',', {pizza_size}, ', and', {pizza_price}, ' Added Successfully.')
#             return render(request, 'results.html', {'result': messages}, {'user': 'Admin'})
#
# def add_soda(request):
#
#     if request.method == 'POST':
#         soda_name = request.POST['soda_name']
#         soda_size = request.POST['soda_size']
#         soda_price = request.POST['soda_price']
#
#         if soda_size == '12 Oz' or '2 Litter':
#             messages.info(request, 'Soda Size needs to be either 12 Oz or 2 Litter')
#             return redirect('mystore')
#
#         else:
#             messages.info({soda_name}, ',', {soda_size}, ', and', {soda_price}, ' Added Successfully.')
#             return render(request, 'results.html', {'result': messages}, {'user': 'Admin'})
#
# def add_side(request):
#
#     if request.method == 'POST':
#         side_name = request.POST['side_name']
#         side_price = request.POST['side_price']
#
#         else:
#             messages.info(request, {side_name}, ' and', {side_price}, ' Added Successfully.')
#             return render(request, 'results.html', {'result': messages}, {'user': 'Admin'})

