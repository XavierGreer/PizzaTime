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

    def initializeWebPizzaProduct(self):
        # id, product_type, name, slug, available, created, updated, image, priceSm, priceMd, priceLg, sizePizza, priceSodaSm, priceSodaLg, sizeSoda, priceSide, category_id
        entities = (
            0, 'Pizza', 'Peperoni','Peperoni', True, 'May 30, 2021, 6:50 p.m.', 'May 30, 2021, 6:50 p.m.', 'products/2021/04/13/S_PIZPX.jpg', 9.99, 14.99, 19.99, None, 1
        )
        cursorObj = self.dbCon.cursor()
        #cursorObj.execute("INSERT INTO web_pizza_product VALUES(0, 'Peperoni', 'Peperoni', True, 01/01/2021, 01/01/2021, 'products/2021/04/13/S_PIZPX.jpg', 9.99, 14.99, 19.99,0,0,0,0,0, 'pizza','pizza')")

        cursorObj.execute('''INSERT INTO web_pizza_product(id, product_type, name, slug, available, created, updated, image, priceSm, priceMd, priceLg, priceSide, category_id ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', entities)


        self.dbCon.commit()
        # cursorObj.execute('''INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)''', entities)



if __name__ == "__main__":
    db = DatabaseController()
    db.getTables()
    #db.getTableInfo('web_pizza_category')
    #db.initializeWebPizzaProduct()
    #db.getTableInfo('web_pizza_product')