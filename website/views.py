from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from registration.models import *
# from Signup.models import Signup
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json
from django.core.mail import send_mail



# Create your views here.

def home(request):

    return render(request, 'index.html', {})

otp=""
@csrf_exempt
def send_otp(request):
    global otp
    if request.method=="POST":
        import random
        import smtplib
        import string
        from email.mime.text import MIMEText

        # generate a random 5-letter OTP
        otp = ''.join(random.choices(string.digits, k=5))

        # create message
        data = json.loads(request.body)
        email = data['email']
        from_email = "sajidahsan67@gmail.com"
        password = "btjvcelmsuhxdmsz"
        subject = "State Life OTP"
        body = f"Thank you for choosing our service.\n\n Your OTP is {otp}.\n\n Please enter this OTP in the verification field to complete the process.\n\nPlease note that this OTP is valid for a limited time and will expire after one time\n\n.If you did not request this OTP or if you have any concerns, please contact our support team immediately.\nThank you for choosing our service.\nBest regards,\nState life company"

        try:
            send_mail(subject, body, from_email, [email], fail_silently=False)
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
@csrf_exempt
def checkOTP(request):

    global otp
    if request.method=="POST":
            data = json.loads(request.body)
            print(data['otp'])
            print(otp,"global")
            if str(otp)==str(data['otp']):
                return JsonResponse({'status': 'success', 'message': "Re-enter the OTP"})
            
            
            else:
                try:
                    return JsonResponse({'status': 'error', 'message': "Re-enter the OTP"})
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': str(e)})
                

def form(request):
    return render(request, 'form.html',{})  

def payPremium(request):
    return render(request, 'payPremium.html',{})        

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
        
        
    
       
        team_name = request.POST.get('teamname')
        team_email = request.POST.get('emailteam')
        team_pas = request.POST.get('teampass')
        team=team_register()
        
        

            
    
        
        
        team.team_name=team_name
        team.team_email=team_email
        team.team_password=team_pas
        team.save()
        
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
                    client = register.objects.get(user_name=login_email,user_password=login_pwd)
                    return redirect("loggedin")
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
    
    return render(request, 'login.html', {})


def jevansaathi(request):
    return render(request, 'jevansaathi.html', {})


def WholeLifeAssurance(request):
    return render(request, 'WholeLifeAssurance.html', {})


def Sadabahar(request):
    return render(request, 'Sadabahar.html', {})


def ChildProtection(request):
    return render(request, 'ChildProtection.html', {})

def onlogin(request):
    return render(request, 'indexlogin.html', {})