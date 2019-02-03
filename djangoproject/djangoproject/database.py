import pyrebase
from .config import config

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def addData(username,themeID):
    data = {"name": username}
    db.child('users').push(data)

def retrieveData(username,themID):
    users = db.child("users").get()
    print(users.val())