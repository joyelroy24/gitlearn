from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate
# Create your views here.
from movies import views

def reg(request):
    error_msg=None
    if request.POST:
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        try:
            user=User.objects.create_user(username=uname,password=pwd)
        except Exception as e:
            error_msg=str(e)

    return render(request,'user_reg.html')

def log(request):
    if request.POST:
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        user=authenticate(username=uname,password=pwd)
        if user:
            print("%%%%%%%%%%%%%%%%%%%%%%")
            authlogin(request,user)
            return redirect('list')

    return render(request,'login.html')


def logout(request):
    authlogout(request)
    print("outtttt")
    return redirect('login')