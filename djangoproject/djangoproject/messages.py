from datetime import datetime

class Message:

    def __init__(self, s, m, p,t):
        self.sender = s
        self.timeStamp = t
        self.text = m
        self.type = p

class Conversation:

    def __init__(self, t, k,r, i):
        self.title = t
        self.timeStamp = k
        self.recipients = r
        self.id = i
        self.dateTimeStamp = datetime.utcfromtimestamp(k)
    def setTime(self, m):
        self.timeStamp = m
        self.dateTimeStamp = datetime.utcfromtimestamp(m)
