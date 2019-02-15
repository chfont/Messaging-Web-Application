
# Sort lambdas
leastTitle = lambda a, b: 1 if a.title < b.title else 0
bigTitle = lambda a, b: 1 if a.title > b.title else 0
recentChat = lambda a, b: 1 if a.timeStamp > b.timeStamp else 0
oldChat = lambda a, b: 1 if a.timeStamp < b.timeStamp else 0
least = lambda a, b: 1 if a < b else 0

def sort(c, cmp):
    length = len(c)
    if length < 2:
        return c
    right = []
    left = []
    for i in range(0,round(length/2.0)):
        left.append(c[i])
    for i in range(round(length/2.0), length):
        right.append(c[i])
    le = sort(left, cmp)
    ri = sort(right, cmp)
    m = merge(le, ri, cmp)
    return m

#Merge 2 lists back together
def merge(l,r,cmp):
    m = []
    i=0
    j=0
    while ((i < len(l)) & (j < len(r))):
        if cmp(l[i], r[j]) == 1:
            m.append(l[i])
            i+= 1
        else:
            m.append(r[j])
            j+=1
    if i == len(l):
        while (j < len(r)):
            m.append(r[j])
            j+= 1
    else:
        while (i < len(l)):
            m.append(l[i])
            i+=1
    return m

def sortConv(id,cv):
    if id == '0':
        cv = sort(cv, leastTitle)
    elif id == '1':
        cv = sort(cv, bigTitle)
    elif id == '2':
        cv = sort(cv, recentChat)
    elif id == '3':
        cv = sort(cv, oldChat)
    return cv
