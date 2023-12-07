from django.shortcuts import render
from . models import Movieinfo
# Create your views here.

def create(request):
    print(request.method)
    if request.POST:
        print(request.POST)
        print(type(request.POST))
        print(request.POST['name'])
        print(request.POST.get('y'))
        if request.POST.get('name'):
            ob_movie=Movieinfo(title=request.POST['name'])
            ob_movie.save()

    return render(request,'create.html')


def list(request):
    
    data=Movieinfo.objects.all()
    print(data)
   

    return render(request,'list.html',{'movies':data})


def delete(request):
    return render(request,'delete.html')