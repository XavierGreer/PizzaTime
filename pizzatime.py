import os
import platform
import subprocess
from databaseController import DatabaseController
import sys # use this library for creating future commend line arguments

def deleteDatabase():
    if platform.system() == 'Windows':
        os.system('del /f db.sqlite3')
    else:
        os.system('rm db.sqlite3')

def updateMigration():
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')

def createSuperUser():
    # p = subprocess.Popen(['python', 'manage.py', 'createsuperuser'],
    #                      stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # p.stdin.write(b"test\n\ntest\ntest\ny\n")
    # p.communicate(input='test\n\ntest\ntest\ny\n')
    #p.stdin.close()
    #os.system(p)
    os.system('python manage.py createsuperuser')

def deleteMigrations():
    for i in os.listdir('web_pizza/migrations/'):
        if i[0:2] != '__':
            os.remove('web_pizza/migrations/' + i)

def runserver():
    os.system('python manage.py runserver')

def populateDatabase():
    db = DatabaseController()
    db.initializeProducts()
    db.initilizeCatagories()
    db.initilizeToppings()
    db.initilizeOrders()


if __name__ == "__main__":
    deleteDatabase()
    deleteMigrations()
    updateMigration()
    #createSuperUser()
    populateDatabase()
    runserver()