from django.shortcuts import render, redirect
import pyrebase
from .forms import LoginForm, NewUser, NewConv
from .config import config
from .database import *

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def login(request):
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
                request.session['theme'] = userTheme
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
                    addData(user['localId'], form.cleaned_data['username'], form.cleaned_data['email'], 0)
                    print("Added data")
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
    form = NewConv()
    return render(request,'./appInterface.html', {'form': form})
def settings(request):
    return render(request, './settings.html')
