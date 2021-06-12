from django.urls import path
from . import views

app_name = 'mystore'

urlpatterns = [
    path('mystore/', views.mystore, name='mystore'),
    path('lookup_products', views.lookup_products, name='lookup_products'),
    path('delete_product/<str:pk>', views.delete_product, name='delete_product'),
    path('update_product/<str:pk>', views.update_product, name='update_product'),
    path('create_customer', views.create_customer, name='create_customer'),
    path('update_customer/<str:pk>', views.update_customer, name='update_customer'),
    path('delete_customer/<str:pk>', views.delete_customer, name='delete_customer'),
    path('lookup_customer/', views.lookup_customer, name='lookup_customer'),
    path('lookup_customer/<str:pk>', views.lookup_customer, name='lookup_customer_byID'),
    path('create_order', views.create_order, name='create_order'),
    path('update_order/<str:pk>', views.update_order, name='update_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),
    path('lookup_order', views.lookup_order, name='lookup_order'),
    path('sideyeah', views.sideyeah, name='sideyeah'),
    path('sodayeah', views.sodayeah, name='sodayeah'),
    path('pizzayeah', views.pizzayeah, name='pizzayeah'),
    path('toppingyeah', views.toppingyeah, name='toppingyeah'),

]