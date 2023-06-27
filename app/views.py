from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'index.html')

######################################################################################
#AUTHENTICATION
def loginUser(request):
    if(request.method=='POST'):
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        print(name,pwd)
        user= authenticate(username=name,password=pwd)
        if(user is not None):
            login(request,user)
            return render(request,'dashboard.html',{'name':name})
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
    return render(request,'dashboard.html')



# import itertools
# def getValidPermutations(n):
#     # Write your code here
#     nums = list(range(1,n+1))
#     l = list(itertools.permutations(nums))
#     # print(l)
#     s=0
#     for permutation in l:
#         num=0
#         for i in range(len(permutation)):
#             if((permutation[i]%(i+1)==0) or((i+1)%permutation[i]==0)):num+=1
#         if(num==len(permutation)): s+=1  
#     print(s)     
#     return s    
# getValidPermutations(15)
