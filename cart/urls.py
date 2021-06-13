from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart', views.cart_detail, name='cart_detail'),
    path('checkout', views.cart_checkout, name='checkout'),
    path('add/<str:name>/<str:size>',views.cart_add, name='cart_add'),
    path('remove/<str:name>',views.cart_remove,name='cart_remove'),
    path('update/<int:id>/<str:status>', views.cart_update, name='cart_update')
]