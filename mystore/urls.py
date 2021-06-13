from django.urls import path
from . import views

app_name = 'mystore'

urlpatterns = [
    path('mystore/', views.mystore, name='mystore'),
    path('lookup_products', views.lookup_products, name='lookup_products'),
    path('delete_soda/<str:pk>', views.delete_soda, name='delete_soda'),
    path('delete_side/<str:pk>', views.delete_side, name='delete_side'),
    path('delete_pizza/<str:pk>', views.delete_pizza, name='delete_pizza'),
    path('delete_topping/<str:pk>', views.delete_topping, name='delete_topping'),
    path('update_side/<str:pk>', views.update_side, name='update_side'),
    path('update_soda/<str:pk>', views.update_soda, name='update_soda'),
    path('update_pizza/<str:pk>', views.update_pizza, name='update_pizza'),
    path('update_topping/<str:pk>', views.update_topping, name='update_topping'),
    path('create_customer', views.create_customer, name='create_customer'),
    path('update_customer/<str:pk>', views.update_customer, name='update_customer'),
    path('delete_customer/<str:pk>', views.delete_customer, name='delete_customer'),
    path('lookup_customer/', views.lookup_customer, name='lookup_customer'),
    path('create_order', views.create_order, name='create_order'),
    path('update_order/<str:id>', views.update_order, name='update_order'),
    path('delete_order/<str:id>', views.delete_order, name='delete_order'),
    path('lookup_order', views.lookup_order, name='lookup_order'),
    path('sideyeah', views.sideyeah, name='sideyeah'),
    path('sodayeah', views.sodayeah, name='sodayeah'),
    path('pizzayeah', views.pizzayeah, name='pizzayeah'),
    path('toppingyeah', views.toppingyeah, name='toppingyeah'),

]