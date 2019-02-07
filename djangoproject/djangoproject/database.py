import pyrebase, json
from .config import config



def addData( username, email, themeID):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    data = {"name": username, "email": email, "themeID": themeID}
    db.child('users').child(username).set(data)

def retrieveData(username,themeID):
    users = db.child("users").get()
    print(users.val())
