import os
import platform
import sys # use this library for creating future commend line arguments

def deleteDatabase():
    if platform.system() == 'Windows':
        os.system('del /f db.sqlite3')
    else:
        os.system('rm db.sqlite3')

def updateDatabase():
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')

def createSuperUser():
    # p = subprocess.Popen(['python', 'manage.py', 'createsuperuser'],
    #                      stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # p.stdin.write(b"test\n\ntest\ntest\ny\n")
    # p.communicate(input='test\n\ntest\ntest\ny\n')
    # p.stdin.close()
    # os.system(p)
    os.system('python manage.py createsuperuser')

def runserver():
    os.system('python manage.py runserver')

if __name__ == "__main__":
    deleteDatabase()
    updateDatabase()
    createSuperUser()
    runserver()