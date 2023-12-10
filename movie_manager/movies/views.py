from django.shortcuts import render,redirect
from . models import Movieinfo
# Create your views here.
from . forms import MovieForm

 

def create(request):
    frm=MovieForm()
    print(request.method)
    print(request.FILES)
    if request.POST:
        print(request.POST)
        title=request.POST.get('title')
        img=request.FILES['image']
        object = Movieinfo(image=img,title=title)
        object.save()

        # frm=MovieForm(request.POST,request.FILES)
        # if frm.is_valid:
        #     frm.save()
    else:
        frm=MovieForm()
        

    return render(request,'create.html',{'frm':frm})


def list(request):
    
    print(request.method)
    print(request.GET)
    if 'action' in request.GET:
        action=request.GET['action']
        print(action)
        id=request.GET['id']
    else:
        action=None
    if action:
        if action=='delete':
            print(id)
            print("^^^^^^^^^^^^^^^^^^^^")
            object=Movieinfo.objects.get(pk=id)
            object.delete()
    data=Movieinfo.objects.all()
   

    return render(request,'list.html',{'movies':data})


def delete(request,pk):
    ob=Movieinfo.objects.get(pk=pk)
    ob.delete()
    data=Movieinfo.objects.all()
    return render(request,'list.html',{'movies':data})

def edit(request,pk):
    object=Movieinfo.objects.get(pk=pk)
    if request.POST:
        # title=request.POST.get('title')
        # object.title=title
        # object.save
        frm=MovieForm(request.POST,instance=object)
        if frm.is_valid():
            frm.save()
        
    
    frm=MovieForm(instance=object)
    # return redirect(create)
    return render(request,"edit.html",{'frm':frm})