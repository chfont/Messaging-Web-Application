from django.shortcuts import render, redirect
import pyrebase
from .forms import *
from .config import config
from .database import *
from .messages import *
from .sort import *
from Crypto.Hash import SHA256
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def login(request):
    request.session.flush()
    if (request.method == 'POST'):
        #Data has been submitted
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = auth.sign_in_with_email_and_password(form.cleaned_data['user'], form.cleaned_data['passcode'])
                uuid = user['localId']
                udata = retrieveUserData(uuid)
                userTheme = udata['themeID']
                request.session['uid'] = uuid
                request.session['themeCSS'] = userTheme+ ".css"
                request.session['username'] = udata['name']
            except:
                error = "Invalid Credentials Entered, Please Try Again"
                form = LoginForm()
                return render(request, './login.html', {'form' : form}, {'error' : error})
            return redirect(appInterface)
        else:
            return redirect(login)
    else:
        form = LoginForm()
    return render(request, './login.html', {'form' : form})
def newuser(request):
    if (request.method == 'POST'):
        form = NewUser(request.POST)
        if form.is_valid():
            if(form.cleaned_data['password'] != form.cleaned_data['confirmPassword']):   #Is this secure?
                return redirect(newuser)
            else:
                #Valid data probably
                try:
                    user = auth.create_user_with_email_and_password(form.cleaned_data['email'], form.cleaned_data['password'])
                    addData(user['localId'], form.cleaned_data['username'], form.cleaned_data['email'], 'default')
                    print("Added data")
                    request.session['uid'] = user['localId']
                    request.session['theme'] = 'default'
                    request.session['themeCSS'] = request.session['theme']+".css"
                    request.session['username']= form.cleaned_data['username']
                except:
                    form = NewUser()
                    return render(request, './registeruser.html', {'form': form})
                return redirect(appInterface)
        else:
            return redirect(newuser)
    else:
        form = NewUser()
    return render(request, './registeruser.html', {'form': form})
def resetpassword(request):
    return render(request, './resetpassword.html')
def rootToLogin(request):
    return redirect(login)

def appInterface(request):
    request.session['currConv'] = "INTENTIONALLY_INVALID_STRING"
    #Need to update ConvList Here
#    convs = getConvs(request.session['uid'],request.session['username'])
#    convos = []
#    if convs != None:
#        for c in convs:
#            convos.append(Conversation(convs[c]['name'], convs[c]['lastSent']))
    convos = pollConvs(request.session['uid'], request.session['username'])
    convos = sortConv('0', convos)
    if(request.method =='POST'):
        form = NewConv(request.POST)
        sort = SortSelect(request.POST)
        enter = ConvEnter(request.POST)
        if(form.is_valid()):
            encKey = SHA256.new(form.cleaned_data['key'].encode('utf-8')).hexdigest()
            newConv = addConv(request.session['uid'], form.cleaned_data['title'], encKey, form.cleaned_data['recipients'], request.session['username'])
            convos = pollConvs(request.session['uid'], request.session['username'])
            convos = sortConv('0', convos)
        elif(sort.is_valid()):
            convos = sortConv(sort.cleaned_data['sortId'], convos)
        elif(enter.is_valid()):
            request.session['currconv'] = str(enter.cleaned_data['convID'])
            request.session['convTitle'] = getConvTitle(request.session['currconv'])
            request.session['convRecip'] = getConvRecipients(request.session['currconv'])
            encKey = SHA256.new(enter.cleaned_data['key'].encode('utf-8')).hexdigest()
            if checkID(enter.cleaned_data['convID'], request.session['uid'], encKey):
                return redirect(displayChat)
            else:
                form = NewConv()
                sort = SortSelect()
                enter = ConvEnter()
    else:
        form = NewConv()
        sort = SortSelect()
        enter = ConvEnter()
    return render(request,'./appInterface.html', {'form': form, 'sort':sort, 'convs': convos,'enter':enter, 'themeCSS': request.session['themeCSS']})

def settings(request):
    if(request.method== 'POST'):
        form = ThemeSelect(request.POST)
        if form.is_valid():
            print(form.cleaned_data['id'])
            updateThemeID(request.session['uid'], form.cleaned_data['id'])
            request.session['theme'] = form.cleaned_data['id']
            request.session['themeCSS'] = request.session['theme'] +".css"
            request.session.modified = True
    else:
        form = ThemeSelect()

    return render(request, './settings.html', {'form': form, 'themeCSS': request.session['themeCSS']})

def displayChat(request):
    return render(request, './convo.html')

def msgbox(request):
    m = getMessages(request.session['currconv'])
    messages = []
    for n in m:
        if m[n]['type'] == 1:
            g = Picto(m[n]['sender'], m[n]['data'],m[n]['type'], m[n]['timeStamp'])
        else:
            g = Message(m[n]['sender'], m[n]['data'], m[n]['type'], m[n]['timeStamp'])
        messages.append(g)
    messages = sortMSGByTime(messages)
    return render(request, './msgbox.html', {'messages': messages})
