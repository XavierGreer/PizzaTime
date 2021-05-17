from django.urls import path
from . import views

app_name = 'mystore'

urlpatterns = [
    path('', views.mystore, name='mystore'),
    path('mystore/', views.mystore, name='mystore'),
    path('mystore/add_topping', views.add_topping, name='add_topping'),
    path('mystore/add_pizza', views.add_pizza, name='add_pizza'),
    path('mystore/add_soda', views.add_soda, name='add_soda'),
    path('mystore/add_side', views.add_side, name='add_side'),
    # path('mystore/edit_customer', views.edit_customer, name='edit_customer'),
    # path('mystore/edit_order', views.edit_order, name='edit_order')
]