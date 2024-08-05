from django.shortcuts import  render,redirect,HttpResponse
# from datetime import datetime
# from home.models import Firsts
from django.contrib.auth import authenticate,logout,login
# from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
@login_required(login_url='loginuser')
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        emailid=request.POST.get('emailid')
        pass1=request.POST.get('pass1')
        my_user=User.objects.create_user(username,emailid,pass1)
        my_user.save()
        return redirect('loginuser')
    return render(request,'signup.html')

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            return render(request,'loginuser.html')
        
        
    #  login.save()
        # messages.success(request, "you have successfully signed in!")
    return render(request,'loginuser.html')

def indexx(request):
    return render(request,'indexx.js')

def first(request):
    return render(request,'first.html')

# def firsts(request):
#     if request.method=="POST":
#         username1=request.POST.get('username1')
#         password1=request.POST.get('password1')
#         firsts=Firsts(username1=username1,password1=password1)
#         firsts.save()
#         firsts = authenticate(request,username1=username1,password1=password1)
#         if firsts is not None:
#             login(request,firsts)
#             return redirect('firsts')
#         else:
#             return render(request,'main.html')
#     return render(request,'firsts.html')

def main(request):
    return render(request,'main.html')

def mainn(request):
    return render(request,'mainn.js')

def style(request):
    return render(request,'style.css')

def style2(request):
    return render(request,'style2.css')