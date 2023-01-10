from django.shortcuts import redirect, render
# Create your views here.

def home(request):
    return render(request, 'index.html',{})


def login(request):
    return render(request,"login.html",{})