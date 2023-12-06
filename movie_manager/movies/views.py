from django.shortcuts import render

# Create your views here.

def create(request):
    return render(request,'create.html')


def list(request):
    return render(request,'list.html')


def delete(request):
    return render(request,'delete.html')