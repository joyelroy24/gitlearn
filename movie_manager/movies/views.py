from django.shortcuts import render
from . models import Movieinfo
# Create your views here.
from . forms import MovieForm
 

def create(request):
    frm=MovieForm()
    print(request.method)
    if request.POST:
        frm=MovieForm(request.POST)
        if frm.is_valid:
            frm.save()
    else:
        frm=MovieForm()
        

    return render(request,'create.html',{'frm':frm})


def list(request):
    
    data=Movieinfo.objects.all()
    print(data)
   

    return render(request,'list.html',{'movies':data})


def delete(request):
    return render(request,'delete.html')