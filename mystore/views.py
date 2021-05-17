from django.shortcuts import render


def mystore(request):
    return render(request, 'mystore.html', {'user': 'Admin'})

#      lists = ['Topping', 'Pizza', 'Sodas', 'Sides', 'Order', 'Customer']

def add_topping(request):

    val1 = request.POST['topping-name']
    res1 = {val1}, " Added Successfully."

    return render(request, 'results.html', {'result': res1}, {'user': 'Admin'})

def add_pizza(request):

    val1 = request.POST['pizza-name']
    val2 = request.POST['pizza-size']
    val3 = request.POST['pizza-price']
    res2 = {val1}, ",", {val2}, ", and", {val3}, " Added Successfully."

    return render(request, 'results.html', {'result': res2}, {'user': 'Admin'})

def add_soda(request):

    val1 = request.POST['soda-name']
    val2 = request.POST['soda-size']
    val3 = request.POST['soda-price']
    res3 = {val1}, ",", {val2}, ", and", {val3}, " Added Successfully."

    return render(request, 'results.html', {'result': res3}, {'user': 'Admin'})

def add_side(request):

    val1 = request.POST['side-name']
    val2 = request.POST['side-price']
    res4 = {val1}, ",", {val2}, " Added Successfully."

    return render(request, 'results.html', {'result': res4}, {'user': 'Admin'})

# def edit_order(request):
#     return render(request, 'orderlookup.html', {'result': 'Success'})
#
# def edit_customer(request):
#     return render(request, 'customerlookup.html', {'result': 'Success'})