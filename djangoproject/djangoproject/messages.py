from datetime import datetime

class Message:

    def __init__(self, s, m):
        self.sender = s
        self.timeStamp = datetime.now()
        self.text = m


class Conversation:

    def __init__(self, t, k,r):
        self.title = t
        self.timeStamp = k
        self.recipients = r
        self.dateTimeStamp = datetime.utcfromtimestamp(k)
    def setTime(self, m):
        self.timeStamp = m
        self.dateTimeStamp = datetime.utcfromtimestamp(m)
