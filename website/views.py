from django.shortcuts import redirect, render
# Create your views here.

def home(request):
    return render(request, 'index.html',{})
def form(request):
    return render(request, 'form.html',{})  

def notification(request):
    
    clients=['Jhon',"ali","umer","qasim"]
    color=["alert-primary","alert-success","alert-info","alert-warning","alert-danger","alert-success","alert-secondary"]

    
    return render(request, 'Notification.html',{"clients":clients,"color":color})   

def RiskAssessment(request):
    return render(request, 'RiskAssessment.html',{})    


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
