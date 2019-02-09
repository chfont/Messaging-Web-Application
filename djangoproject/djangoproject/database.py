import pyrebase, json
from .config import config


firebase = pyrebase.initialize_app(config)
db = firebase.database()

def addData( id, username, email, themeID):

    data = {"name": username, "email": email, "themeID": themeID}
    db.child('users').child(id).set(data)

def retrieveData(username,themeID):
    users = db.child("users").get()
    print(users.val())
