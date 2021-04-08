from django.contrib import admin
from .models import Category, Product, Topping, Pizza, ToppingAmount, Soda, Sides, Order, Customer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','available','created','updated']
    list_filter = ['available','created','updated']
    list_editable = ['price','available']
    prepopulated_fields = {'slug': ('name',)}

class ToppingAmountInline(admin.TabularInline):
    model = ToppingAmount

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name','size','price']
    inlines = [ToppingAmountInline, ]

@admin.register(Soda)
class SodaAdmin(admin.ModelAdmin):
    list_display = ['name','size','price']

@admin.register(Sides)
class SidesAdmin(admin.ModelAdmin):
    list_display = ['name','price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['orderID', 'customer', 'status', 'total', 'discount',]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customerID', 'firstname', 'lastname', 'phone', 'email', 'address', 'zipcode']

'''
Admin test account information.
Username: Test
Password: test
'''