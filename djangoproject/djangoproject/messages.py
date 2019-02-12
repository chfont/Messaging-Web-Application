from datetime import datetime

class Message:

    def __init__(self, s, m):
        self.sender = s
        self.timeStamp = datetime.now()
        self.text = m


class Conversation:

    def __init__(self, t, k):
        self.title = t
        self.timeStamp = k
