from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    '''def get_absolute_url(self):
        return reverse('web_pizza:product_list_by_category',args=[self.slug])'''


class Topping(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'topping'
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.name

'''
class Pizza(models.Model):
    price_small = models.DecimalField(max_digits=8, decimal_places=2)
    price_big = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=60)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE, blank=True)
    PIZZA_SIZES = (
        (12, 'Medium'),
        (16, 'Large'),
    )

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=10)


class Order(models.Model):
    pizza = models.ForeignKey('main.Pizza', on_delete=models.PROTECT)
    size = models.IntegerField(choices=Pizza.PIZZA_SIZES, default=30, blank=False)
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField(null=False, blank=False)

    @property
    def price(self):
        """ Returns the price of the order. """
        if self.size == 30:
            return self.pizza.price_small
        if self.size == 50:
            return self.pizza.price_big
        return self.pizza.price_small
'''

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
        return reverse('web_pizza:product_detail_by_category',args=[self.id,self.slug])

