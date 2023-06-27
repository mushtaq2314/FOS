from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'index.html')

######################################################################################
#AUTHENTICATION
global uname
def loginUser(request):
    if(request.method=='POST'):
        global uname
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        print(uname,pwd)
        user= authenticate(username=uname,password=pwd)
        if(user is not None):
            login(request,user)
            return render(request,'dashboard.html',{'name':uname})
        else:
            return render(request,'login.html',{'msg':'Invalid Credentials!'})
    return render(request,'login.html')
def signupUser(request):
    if(request.method=='POST'):
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        uname= request.POST.get('username')
        # email= request.POST.get('email')
        pwd= request.POST.get('password')
        user=User.objects.create_user(username=uname,password=pwd)
        user.first_name=fname
        user.last_name=lname
        user.save()
        return render(request,'dashboard.html',{'name':uname})
    return render(request,'signup.html')
def logoutUser(request):
    logout(request)
    return render(request,'login.html')
######################################################################################
def dashboard(request):
    print(request.user.is_anonymous)
    if(request.user.is_anonymous):
        return render(request,'login.html',{'msg':'Please login first!'})
    global uname
    name=uname
    return render(request,'dashboard.html',{'name':name})


