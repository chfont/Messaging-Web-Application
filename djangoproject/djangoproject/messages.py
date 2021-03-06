from datetime import datetime, timezone


def bHex(hexs):
    dec = int(hexs, 64)
    b = bin(dec)
    b = b[2:]
    if len(b) != 6:
        for i in range(6-len(b)):
            b = "0"+b
    return b

def B64(s):
    charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-"
    decDigi = charset.find(s)
    b = bin(decDigi)
    b = b[2:]
    if len(b) != 6:
        for i in range(6-len(b)):
            b= "0"+b
    return b

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
        self.dateTimeStamp = datetime.fromtimestamp(k, tz=None)
    def setTime(self, m):
        self.timeStamp = m
        self.dateTimeStamp = datetime.fromtimestamp(m, tz=None)


class Picto:
    def __init__(self,s, d, p, t):
        self.type = p
        self.sender = s
        self.raw = d
        self.timeStamp = t
        self.imgData = self.convertData()
    def convertData(self):
        arr = []
        for i in self.raw:
            j = B64(i)
            for n in j:
                arr.append(0)
                arr.append(0)
                arr.append(0)
                if n == "1":
                    arr.append(255)
                else:
                    arr.append(0)
        return arr
