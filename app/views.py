from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return render(request,'index.html',{})
    return HttpResponse("<h1>Hello World !</h1>")
