from django.db import models
from django.urls import reverse
import uuid
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name','slug',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list:product_list_by_category',args=[self.slug])

class Pizza(models.Model):
    name = models.CharField(max_length=60)
    topping = models.ManyToManyField('Topping', through='ToppingAmount')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    PIZZA_SIZES = (
        (12, 'Small'),
        (14, 'Medium'),
        (16, 'Large'),
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.IntegerField(choices=PIZZA_SIZES, default=12, blank=False)

    class Meta:
        ordering = ('name','size')
        verbose_name = 'pizza'
        verbose_name_plural = 'pizzas'

    def __str__(self):
        return self.name

class ToppingAmount(models.Model):
    Nothing = 0
    Regular = 1
    Double = 2
    CHOICES = (
        (Nothing, 'Nothing'),
        (Regular, 'Regular'),
        (Double, 'Double'),
    )

    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE, null=True, blank=True)
    topping = models.ForeignKey('Topping', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(choices=CHOICES, default=Nothing)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list:product_detail',args=[self.id,self.slug])

class Topping(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'topping'
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.name

class Soda(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    SODA_SIZES = (
        (1, '12 Oz'),
        (2, '2 Liter'),
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField(choices=SODA_SIZES, default=12, blank=False)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'size', 'price')
        verbose_name = 'soda'
        verbose_name_plural = 'sodas'

    def __str__(self):
        return self.name

class Sides(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'price',)
        verbose_name = 'side'
        verbose_name_plural = 'sides'

    def __str__(self):
        return self.name

class Customer(models.Model):
    customerID = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=100, editable=False)
    firstname = models.CharField(max_length=50, db_index=True)
    lastname = models.CharField(max_length=50, db_index=True)
    phone = models.CharField(max_length=10, null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    email = models.EmailField(max_length = 254)
    address = models.CharField("Address line 1", max_length=1024,)
    zipcode = models.CharField("ZIP / Postal code", max_length=12, editable=False)

class Order(models.Model):
    orderID = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=100, editable=False)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    tax = models.DecimalField(max_digits=4, decimal_places=2, editable=False)
    discount = models.DecimalField(max_digits=2, decimal_places=0,)
    STATUSES = (
        (0, 'Order Received'),
        (1, 'Baking'),
        (2, 'On The Way'),
        (3, 'Delivered'),
    )
    status = models.IntegerField(choices=STATUSES, default=0, blank=False)

    def __str__(self):
        return str(self.orderID)
