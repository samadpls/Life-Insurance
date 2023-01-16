from django.shortcuts import redirect, render
# Create your views here.

def home(request):
    return render(request, 'index.html',{})


def login(request):
    return render(request,'login.html',{})

def jevansaathi(request):
    return render(request, 'jevansaathi.html',{}) 

def WholeLifeAssurance(request):
    return render(request, 'WholeLifeAssurance.html',{}) 

def Sadabahar(request):
    return render(request, 'Sadabahar.html',{}) 

def ChildProtection(request):
    return render(request, 'ChildProtection.html',{})