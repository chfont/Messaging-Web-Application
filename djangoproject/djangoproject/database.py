import pyrebase, json
from .config import config
from datetime import datetime
from time import time

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def addData( id, username, email, themeID):

    data = {"name": username, "email": email, "themeID": themeID}
    db.child('users').child(id).set(data)

def retrieveUserData(id):
        data = db.child("users").child(id).get()
        return data.val()

def addConv(id, convT, convK):
    data = {"name": convT, "key": convK, "lastSent": time()}
    db.child('users').child(id).child("Conversations").child(data['name']).set(data)

def sortConversationsbyKey(sortKey, id):
    data = db.child("users").child(id).child("Conversations").order_by_child(key).get()
    return data.val()

def updateThemeID(id, val):
    db.child("users").child(id).update({"themeID": val})
