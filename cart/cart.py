from decimal import *
from django.conf import settings
from web_pizza.models import *
from databaseController import DatabaseController


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
        # add the if statement for different prices
        db.addOrderItem(prod.get('priceMd'), size, prod.get('name'))
        addedProd = db.getOrderItem(name)

        item = {'id' : prod.get('id'), 'name' : prod.get('name'), 'price' : prod.get('priceMd'), 'size' : size}
        self.cart.append(item)

        # item['size'] = size
        # self.cart['price'] = prod.get('priceMd')
        # self.cart['name'] = prod.get('name')

        #self.items = db.getOrderItem(prod.get('name'))

        # self.items.append() = db.getOrderItems()

        # for item in self.items:
        #     price = str(item[1])
        #     if price not in self.cart:
        #         self.cart[price] =  item[1]
        #         self.cart[name] = item[2]

        self.save()

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
        # product_ids = (item.get('id') for item in self.cart
        db = DatabaseController()
        products = self.cart

        cart = self.cart.copy()

        # for product in products:
        #     # print(cart[product][0])
        #     cart[product] = product

        for item in self.cart:
            for i in item.value():
                i['price'] = Decimal(i['price'])
                self.total = i['price'] * len(self.cart)
                yield item
    # def __iter__(self):
    #
    #     return range(self.cart)


    def __len__(self):
        return len(self.cart)

    def get_total_price(self):
        for item in self.cart:
            self.total = self.total + item.get('price')
        return self.total

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
