from django.db import models
from django.urls import reverse
import uuid
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.contrib.auth import get_user_model

class Category(models.Model):
    NAME_CHOICES = [
        ('Pizza', 'Pizza'),
        ('Soda', 'Soda'),
        ('Side', 'Side')
    ]
    name = models.CharField(max_length=200, choices=NAME_CHOICES, db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name','slug',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('web_pizza:product_list_by_category',args=[self.slug])

PIZZA_SIZES = (
        (12, 'Small'),
        (14, 'Medium'),
        (16, 'Large'),
    )

SODA_SIZES = (
        (1, '12 Oz'),
        (2, '2 Liter'),
    )

TYPE_CHOICES = [
        ('Pizza', 'Pizza'),
        ('Soda', 'Soda'),
        ('Side', 'Side'),
    ]

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    product_type = models.CharField(max_length=25, choices=TYPE_CHOICES, default=None)

    # Common Fields
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', default='no_img.jpg')

    # Pizza Fields

    topping = models.ManyToManyField('Topping', through='ToppingAmount')
    priceSm = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    priceMd = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    priceLg = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    #Sides Fields
    priceSide = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('web_pizza:product_detail',args=[self.id, self.slug])

class PizzaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(product_type='Pizza')

class Pizza(Product):
    objects = PizzaManager()

    class Meta:
        proxy = True
        verbose_name = 'pizza'
        verbose_name_plural = 'pizzas'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.product_type = 'Pizza'
        return super(Pizza, self).save(self.id, self.slug)


class SodaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(product_type='Soda')

class Soda(Product):
    objects = SodaManager()

    class Meta:
        proxy = True
        verbose_name = 'soda'
        verbose_name_plural = 'sodas'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.product_type = 'Soda'
        return super(Soda, self).save(*args, **kwargs)

class SidesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(product_type='Side')

class Side(Product):
    objects = SidesManager()

    class Meta:
        proxy = True
        verbose_name = 'side'
        verbose_name_plural = 'sides'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.product_type = 'Side'
        return super(Side, self).save(*args, **kwargs)

class ToppingAmount(models.Model):
    Regular = 1
    Double = 2
    CHOICES = (
        (Regular, 'Regular'),
        (Double, 'Double'),
    )
    pizza = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
    topping = models.ForeignKey('Topping', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(choices=CHOICES, default=Regular)

class Topping(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'topping'
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.name

class Customer(models.Model):
    customerID = models.CharField("Customer ID", primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=100, editable=False)
    firstname = models.CharField("First Name", max_length=50, db_index=True, editable=True)
    lastname = models.CharField("Last Name", max_length=50, db_index=True, editable=True)
    phone = models.CharField("Phone", max_length=12, null=True, validators=[RegexValidator(r'^\d{3}(-)?\d{3}(-)?\d{4}$')], editable=True)
    email = models.EmailField("Email", max_length = 254, editable=True)
    address = models.CharField("Address line 1", max_length=1024, editable=True)
    zipcode = models.CharField("ZIP / Postal code", max_length=12, editable=True)



class Order(models.Model):
    orderID = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=100, editable=False)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True, editable=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=True)
    tax = models.DecimalField(max_digits=4, decimal_places=2, editable=True)
    discount = models.DecimalField(max_digits=2, decimal_places=0, editable=True)

    STATUSES = (
        (0, 'Order Received'),
        (1, 'Baking'),
        (2, 'On The Way'),
        (3, 'Delivered'),
    )
    status = models.IntegerField("Order Status", choices=STATUSES, default=0, blank=False, editable=True)

    def __str__(self):
        return str(self.orderID)

class OrderItem(models.Model):
    ProductOrderID = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=100, editable=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sizePizza = models.IntegerField(choices=PIZZA_SIZES, default=12, blank=False)
    name = models.CharField(max_length=200,db_index=True)
    toppings = models.CharField(max_length=200,db_index=True)

    def __str__(self):
        return self.name