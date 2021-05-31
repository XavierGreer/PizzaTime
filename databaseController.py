import sqlite3

class DatabaseController:
    def __init__(self):
        self.dbCon = sqlite3.connect("db.sqlite3")

    def getTables(self):
        cursorObj = self.dbCon.cursor()
        cursorObj.execute('SELECT name from sqlite_master where type= "table"')
        print(cursorObj.fetchall())

    def getTableInfo(self, tablename):
        cursorObj = self.dbCon.cursor()
        cursorObj.execute('SELECT * FROM ' + tablename)
        rows = cursorObj.fetchall()
        if len(rows) < 1:
            print('no rows')
        else:
            for row in rows:
                print(row)

    def initializeProducts(self):
        # id, product_type, name, slug, available, created, updated, image, priceSm, priceMd, priceLg, sizePizza, priceSodaSm, priceSodaLg, sizeSoda, priceSide, category_id
        products = [
                (0, 'Pizza', 'Pepperoni', 'Pepperoni', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.', 'products/2021/04/13/S_PIZPX.jpg', 9.99, 14.99, 19.99, None, 1),
                (1, 'Pizza', 'Hawaiian','Hawaiian', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.', 'products/2021/04/14/S_PIZCR.jpg', 9.99, 14.99, 19.99, None, 1),
                (2, 'Pizza', 'Meat Lover', 'MeatLover', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.', 'products/2021/04/13/S_MX.jpg', 9.99, 14.99, 19.99, None, 1),
                (3, 'Pizza', 'Vegetable', 'Vegetable', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.', 'products/2021/04/19/S_PZTACO.jpg', 9.99, 14.99, 19.99, None, 1),
                (4, 'Pizza', 'Supreme', 'Supreme', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.', 'products/2021/04/19/S_PIZPV_tdiaCz6.jpg', 9.99, 14.99, 19.99, None, 1),
                (5, 'Pizza', 'BBQ Chicken', 'BBQChicken', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.', 'products/2021/04/19/S_PIZCR_RSF3OLf.jpg', 9.99, 14.99, 19.99, None, 1),
                (6, 'Pizza', 'Buffalo Chicken', 'BuffaloChicken', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.', 'products/2021/04/19/S_PIZCK_InLB48q.jpg', 9.99, 14.99, 19.99, None, 1),

                (7, 'Soda', 'Coke', 'Coke', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.','products/2021/04/14/F_COKE.jpg', 9.99, 14.99, 19.99, None, 1),
                (8, 'Soda', 'Diet Coke', 'DietCoke', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.','products/2021/04/14/F_DIET.jpg', 9.99, 14.99, 19.99, None, 1),
                (9, 'Soda', 'Orange', 'Orange', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.','products/2021/04/19/F_ORAN.jpg', 9.99, 14.99, 19.99, None, 1),
                (10, 'Soda', 'Sprite', 'Sprite', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.','products/2021/04/19/F_SPRITE.jpg', 9.99, 14.99, 19.99, None, 1),

                (11, 'Sides', 'Lava Cake', 'LavaCake', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.','products/2021/04/14/F_LAVA.jpg', 9.99, 14.99, 19.99, None, 1),
                (12, 'Sides', 'Bread Sticks', 'BreadSticks', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.','products/2021/04/19/B_Sticks.jpg', 9.99, 14.99, 19.99, None, 1),
                (13, 'Sides', 'Wings', 'Wings', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.','products/2021/04/19/C_Wings.png', 9.99, 14.99, 19.99, None, 1),
                (14, 'Sides', 'Garlic Knots', 'GarlicKnots', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.','products/2021/04/19/G_Knot.jpg', 9.99, 14.99, 19.99, None, 1)
            ]
        cursorObj = self.dbCon.cursor()
        for product in products:
            cursorObj.execute('''INSERT INTO web_pizza_product(id, product_type, name, slug, available, created, updated, image, priceSm, priceMd, priceLg, priceSide, category_id ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', product)
        self.dbCon.commit()

    def initilizeCatagories(self):
        catagories = [
            (0, 'Pizza', 'Pizza'),
            (1, 'Soda', 'Soda'),
            (2, 'Side', 'Side')
        ]
        cursorObj = self.dbCon.cursor()
        for catagory in catagories:
            cursorObj.execute(
                '''INSERT INTO web_pizza_category(id, name, slug) VALUES(?, ?, ?)''',
                catagory)
        self.dbCon.commit()

    def initilizeToppings(self):
        toppings = [
            (0, 'Pepperoni'), (1, 'Mushrooms'), (2, 'Sausage'), (3, 'Onions'), (4, 'Bacon'), (5, 'Extra Cheese'),
            (6, 'Peppers'), (7, 'Black Olives'), (8, 'Chicken'), (9, 'Pineapple'), (10, 'Spinach'), (11, 'Fresh Basil'),
            (12, 'Ham'), (13, 'Pesto'), (14, 'Beef'), (15, 'Artichoke'), (16, 'Spinach'), (17, 'Anchovies'),
            (18, 'Tomatoes'), (19, 'Sun-Dried Tomatoes')
        ]
        cursorObj = self.dbCon.cursor()
        for topping in toppings:
            cursorObj.execute(
                '''INSERT INTO web_pizza_topping(id, name) VALUES(?, ?)''',
                topping)
        self.dbCon.commit()


if __name__ == "__main__":
    db = DatabaseController()
    db.getTables()
    #db.getTableInfo('web_pizza_category')
    #db.initializeWebPizzaProduct()
    #db.getTableInfo('web_pizza_product')