from django.urls import path
from . import views

app_name = 'mystore'

urlpatterns = [
    path('mystore/', views.mystore, name='mystore'),
    path('results/', views.results, name='results'),
    path('edit_customer', views.edit_customer, name='edit_customer'),
    path('edit_order', views.edit_order, name='edit_order')
    # path('mystore/add_topping', views.add_topping, name='add_topping'),
    # path('mystore/add_pizza', views.add_pizza, name='add_pizza'),
    # path('mystore/add_soda', views.add_soda, name='add_soda'),
    # path('mystore/add_side', views.add_side, name='add_side'),

]