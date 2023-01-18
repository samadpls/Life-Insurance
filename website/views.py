from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from registration.models import register
# from Signup.models import Signup

from django.contrib.auth import get_user_model



# Create your views here.

def home(request):
<<<<<<< HEAD
    return render(request, 'index.html', {})
=======
    return render(request, 'index.html',{})
def form(request):
    return render(request, 'form.html',{})  

def notification(request):
    
    clients=['Jhon',"ali","umer","qasim"]
    color=["alert-primary","alert-success","alert-info","alert-warning","alert-danger","alert-success","alert-secondary"]

    
    return render(request, 'Notification.html',{"clients":clients,"color":color})   

def RiskAssessment(request):
    return render(request, 'RiskAssessment.html',{})    
>>>>>>> a94a416520141181fe177c68a1be06015e8dd17e


@csrf_exempt
def login(request):
    
    
    
    
    
        
        

    if request.method == 'POST':
        print('hello1')

        type1 = request.POST.get('email')
        type2 = request.POST.get('password')

        type3 = request.POST.get('cpassword')

        if type2 == type3:
            data = register()
            data.user_name = type1
            data.user_password = type2
            data.save()
            
            
            # print('hello2')
           
            
            # if get_user_model().objects.filter(type1=type1).exists():
            #     print('masla ha')
            
        
            
            
        
        
            
        

       

    
    
    return render(request, 'login.html', {})


def jevansaathi(request):
    return render(request, 'jevansaathi.html', {})


def WholeLifeAssurance(request):
    return render(request, 'WholeLifeAssurance.html', {})


def Sadabahar(request):
    return render(request, 'Sadabahar.html', {})


def ChildProtection(request):
<<<<<<< HEAD
    return render(request, 'ChildProtection.html', {})
=======
    return render(request, 'ChildProtection.html',{})
>>>>>>> a94a416520141181fe177c68a1be06015e8dd17e
