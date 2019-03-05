import pyrebase, json
from .config import config
from datetime import datetime
from time import time
from .messages import *
from Crypto import Random
from Crypto.Hash import SHA256

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def addData( id, username, email, themeID):

    data = {"name": username, "email": email, "themeID": themeID, "uid": id}
    db.child('users').child(id).set(data)

def retrieveUserData(id):
        data = db.child("users").child(id).get()
        return data.val()

def addConv(id, convT, convK, convRs, username):
    reps = convRs.split(",")
    reps.append(username)
    data = {"name": convT, "key": convK, "lastSent": time(),"recipients": reps}
    data2 = {"name": convT, "lastSent": time(), "recipients": reps}

    rnd = Random.new()
    byt = rnd.read(16)
    byt = int.from_bytes(byt, byteorder='little')
    #check validity here
    data3 = retrieveUserData(id)
    db.child('users').child(id).child("Conversations").child(byt).set(data)
    db.child('Conversations').child(byt).set(data2)
    c = Conversation(data['name'], data['lastSent'], data2['recipients'],byt)
    return c

def getConvs(id,username):
    pollConvs(id,username)
    data = db.child("users").child(id).child("Conversations").get()
    return data.val()

def sortConversationsbyKey(sortKey, id):
    data = db.child("users").child(id).child("Conversations").order_by_child(sortKey).get()
    return data.val()

def updateThemeID(id, val):
    db.child("users").child(id).update({"themeID": val})

def pollConvs(id, username):
    convs=[]
    convList = db.child("Conversations").get().val()
    if convList == None:
        return
    for i in convList:
        if (username in convList[i]['recipients']):
            data = {"chatID": i, "recipients": convList[i]['recipients'],"name": convList[i]['name'], "lastSent": convList[i]['lastSent']}
            c = db.child("users").child(id).child("Conversations").child(i).get().val()
            if c == None:
                k = ""
                enc = SHA256.new(k.encode('utf-8')).hexdigest()
                data2 = data = {"chatID": i, "recipients": convList[i]['recipients'],"name": convList[i]['name'], "lastSent": convList[i]['lastSent'], "key": enc}
                db.child("users").child(id).child("Conversations").child(i).set(data2)
            else:
                db.child("users").child(id).child("Conversations").child(i).update(data)
            print("placeholder")
            c = Conversation(convList[i]['name'],convList[i]['lastSent'], convList[i]['recipients'], i)
            convs.append(c)
    return convs
