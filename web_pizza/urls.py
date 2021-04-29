from django.urls import path
from . import views

app_name = 'web_pizza'

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('<slug:category_slug>',views.menu,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
