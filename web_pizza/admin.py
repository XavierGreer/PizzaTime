from django.contrib import admin
from .models import Category, Product, Topping, Pizza, ToppingAmount, Soda, Side, Order, Customer, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}



'''@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','available']
    list_filter = ['available']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}'''

class ToppingAmountInline(admin.TabularInline):
    model = ToppingAmount

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    fields = ('category','name','image','available','priceSm','priceMd','priceLg')
    inlines = [ToppingAmountInline,]

@admin.register(Soda)
class SodaAdmin(admin.ModelAdmin):
    fields = ('category','name','image','available','priceSodaSm','priceSodaLg')

@admin.register(Side)
class SidesAdmin(admin.ModelAdmin):
    fields = ('category','name','image','available','priceSide')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['orderID', 'customer', 'status', 'total', 'discount',]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customerID', 'firstname', 'lastname', 'phone', 'email', 'address', 'zipcode']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['price','name','size','toppings']
