from databaseController import DatabaseController

class OrderItem:
    def __init__(self, id, name, price, size):
        self.id = id
        self.name = name
        self.price = price
        self.size = size

class OrderItems:
    def __init__(self):
        self.db = DatabaseController()

    def addItem(self, price, size, name):
        self.db.addOrderItem(price, size, name)

    def getAll(self):
        results = self.db.getOrderItems()
        orderItems = []
        for i in results:
            item = OrderItem(i[0], i[3], i[1], i[2])
            orderItems.append(item)
        return orderItems

    def getByName(self, name):
        listObjects = self.getAll()
        for x in listObjects:
            if x.name == name:
                return x

if __name__ == "main":
    d = OrderItems()

    d.addItem(23.33, 'Medium', 'Coke')
    x = d.getAll()
    print('id: ', x[0].id)
    print('size: ', x[0].size)
    print('pice: ', x[0].price)
    print('name: ', x[0].name)
