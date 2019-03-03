import pyrebase, json
from .config import config
from datetime import datetime
from time import time
from .messages import *
from Crypto import Random

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def addData( id, username, email, themeID):

    data = {"name": username, "email": email, "themeID": themeID, "uid": id}
    db.child('users').child(id).set(data)

def retrieveUserData(id):
        data = db.child("users").child(id).get()
        return data.val()

def addConv(id, convT, convK, convRs, uid):
    reps = convRs.split(",")

    data = {"name": convT, "key": convK, "lastSent": time()}
    data2 = {"name": convT, "lastSent": time(), "recipients": reps}
    db.child('users').child(id).child("Conversations").child(data['name']).set(data)
    rnd = Random.new()
    byt = rnd.read(16)
    byt = int.from_bytes(byt, byteorder='little')
    #check validity here
    data3 = retrieveUserData(uid)
    print(data3)
    db.child('Conversations').child(byt).set(data2)
    c = Conversation(data['name'], data['lastSent'])
    return c

def getConvs(id):
    data = db.child("users").child(id).child("Conversations").get()
    return data.val()

def sortConversationsbyKey(sortKey, id):
    data = db.child("users").child(id).child("Conversations").order_by_child(sortKey).get()
    return data.val()

def updateThemeID(id, val):
    db.child("users").child(id).update({"themeID": val})
