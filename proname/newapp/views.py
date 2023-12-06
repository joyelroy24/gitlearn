from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def printhello(request):
    data={}
    data['key']="hello Guyss"
    data['listkey']=[{'key1':'hello'},{'key1':'heyy'}]
    return render(request,'test.html',data) 
