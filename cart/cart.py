from decimal import *
from django.conf import settings
from web_pizza.models import *
from databaseController import DatabaseController
from OrderItem import OrderItems

class Cart(object):
    def __init__(self,request):
        """Initializing Cart"""

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]=[]
        self.cart = cart
        self.order = False
        self.total = 0
        self.id = Order.objects.all().count()

    def add(self, product, size, name):
        db = DatabaseController()
        prod = db.getPruductBySlug(name)
        price = 0
        if prod.get('category') == 'Pizza' or 'Soda':
            if size == 'Small':
                price = prod.get('priceSm')
            elif size == 'Medium':
                price = prod.get('priceMd')
            elif size == 'Large':
                price = prod.get('priceLg')
        elif prod.get('category') == 'Sides':
            if size == 'Small':
                price = prod.get('priceSide')

        db.addOrderItem(self.id, price, size, prod.get('name'))

        orderItems = OrderItems()
        orderItem = orderItems.getByName(prod.get('name'))

        item = dict({'name': prod.get('name'), 'size': size, 'price': price, 'id': self.id})
        self.cart.append(item)
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        for item in self.cart:
            yield item

    def __len__(self):
        return len(self.cart)

    def get_total_price(self):
        self.total = 0
        for item in self.cart:
            self.total += item.get('price')
        return self.total

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def checkout(self):
        db = DatabaseController()
        if self.order == False:
            self.order = True
            db.addOrder(self.get_total_price())
        self.clear()

    def update(self, id, status):
        db = DatabaseController()
        db.updateStatus(id, status)