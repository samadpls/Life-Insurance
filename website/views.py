from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from registration.models import *
# from Signup.models import Signup
from django.contrib import messages
from django.contrib.auth import get_user_model



# Create your views here.

def home(request):

    return render(request, 'index.html', {})

    return render(request, 'index.html',{})
def form(request):
    return render(request, 'form.html',{})  

def notification(request):
    
    clients=['Jhon',"ali","umer","qasim"]
    color=["alert-primary","alert-success","alert-info","alert-warning","alert-danger","alert-success","alert-secondary"]

    
    return render(request, 'Notification.html',{"clients":clients,"color":color})   

def RiskAssessment(request):
    return render(request, 'RiskAssessment.html',{})  

csrf_exempt
def delete_item(request,team_id):
    
    data=team_register.objects.get(team_id=team_id)
    data.delete()

    return redirect('/target')

@csrf_exempt
def target(request):
   

        
    
    if request.method == 'POST':
        team_email = request.POST.get('emailteam')
        if "@teams.com" in team_email:
            team_name = request.POST.get('teamname')
            team_pas = request.POST.get('teampass')
            if len(team_pas)>=5:
                team, created = team_register.objects.get_or_create(
                    emailteam=team_email,team_password=team_pas,team_name=team_name)
                if created:
                    messages.error(request,"Team registered successfully!")
                    return redirect('target')
                
            # team=team_register()
            
            # team.team_name=team_name
            # team.team_email=team_email
            # team.team_password=team_pas
            # team.save()
        
        # return render(request,"target.html")
        
    task=team_register.objects.all()
    
    print(task)
        # task2={'task':task}
        
    return render(request,"target.html",{'task':task})



            
             
@csrf_exempt
def login(request):
    
    if request.method=='GET':
        try:
            login_email=request.GET.get("login_name")
            login_pwd=request.GET.get("login_pwd")
            if "@teams.com" in login_email:
                try:
                    team = team_register.objects.get(team_email=login_email,team_password=login_pwd)
                    return redirect("target")
                except team_register.DoesNotExist:
                    messages.error(request,"Email or password is not correct")
                    return redirect('login')  
            elif "@salesmanager.com" in login_email:
                pass
             
            else:
                try:
                    team = register.objects.get(user_name=login_email,user_password=login_pwd)
                    return redirect("/")
                except register.DoesNotExist:
                    messages.error(request,"Email or password is not correct")
                    return redirect('login')  
                 
        except:
            return render(request,"login.html")

    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        if not( ("@teams.com" or "@salesmanager.com") in email):
            cpwd = request.POST.get('cpassword')
            reg_id=register.objects.all()
            for id in reg_id:
                if id.user_name==email:
                    messages.error(request,"Email already exists")
                    return redirect('login') 

            if pwd == cpwd:
                data = register()
                data.user_name = email
                data.user_password = pwd
                data.save()
                        
            else:
                messages.error(request,"Password doesn't match")
                return redirect('login')
               
        else:
            messages.error(request,"Invalid Email")
            return redirect('login') 
            
            
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
    return render(request, 'ChildProtection.html', {})

