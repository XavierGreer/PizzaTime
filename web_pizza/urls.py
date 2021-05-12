from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'web_pizza'

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('about', views.aboutus, name='aboutus'),
    path('<slug:category_slug>',views.menu,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
