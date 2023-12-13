from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

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