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
        # self.item = {}
        self.total = 0
        # self.quantity = 0

    def add(self, product, size, name):
        db = DatabaseController()
        prod = db.getPruductBySlug(name)
        # addedProd = db.getOrderItem(name)
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

        db.addOrderItem(price, size, prod.get('name'))

        orderItems = OrderItems()
        orderItem = orderItems.getByName(prod.get('name'))

        item = dict({'name': prod.get('name'), 'size': size, 'price': price, 'id': orderItem.id})
        self.cart.append(item)

        self.save()
        # item['size'] = size
        # self.cart['price'] = prod.get('priceMd')
        # self.cart['name'] = prod.get('name')

        # self.items = db.getOrderItem(prod.get('name'))
        # self.items.append() = db.getOrderItems()

        # for item in self.items:
        #     price = str(item[1])
        #     if price not in self.cart:
        #         self.cart[price] =  item[1]
        #         self.cart[name] = item[2]

    # def add(self, product, quantity=1, override_quantity=False):
    #     print("added to cart")
    #     product_id = str(product.id)
    #     if product_id not in self.cart:
    #         self.cart[product_id] = {'quantity': 0, 'price': str(product.priceSm)}
    #
    #     if override_quantity:
    #         self.cart[product_id]['quantity'] = quantity
    #     else:
    #         self.cart[product_id]['quantity'] += quantity
    #     self.save()

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
    #     product_ids = (item.get('id') for item in self.cart
    #     db = DatabaseController()
    #     products = self.cart
    #
    #     cart = self.cart.copy()
    #
    #     for product in products:
    #         # print(cart[product][0])
    #         cart = product
    #
    #     for item in self.cart:
    #         for i in item:
    #             i[0] = i[0]
    #             self.total = i['price'] * len(self.cart)
    #             yield i

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
