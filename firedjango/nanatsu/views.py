from django.shortcuts import render
import pyrebase
from django.contrib import auth
# Create your views here.
config = {
    'apiKey': "AIzaSyANs1uD6cJSACe-xNKO8HcR1fF5lboEs8A",
    'authDomain': "awesome-dbacf.firebaseapp.com",
    'databaseURL': "https://awesome-dbacf.firebaseio.com",
    'projectId': "awesome-dbacf",
    'storageBucket': "awesome-dbacf.appspot.com",
    'messagingSenderId': "601763630874"
  }
firebase=pyrebase.initialize_app(config)
autho=firebase.auth()

def signIn(request):
    return render(request,'signIn.html')

def postsignIn(request):
    email=request.POST.get('email')
    passw=request.POST.get('passwors')
    try:
        user=autho.sign_in_with_email_and_password(email, passw)
    except:
        message='invalid credential'
        return render(request,'signIn.html',{'message':message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,'welcome.html',{"e":email})

def logout(request):
    auth.logout(request)
    return render(request,'signIn.html')
    
