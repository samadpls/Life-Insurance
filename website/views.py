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
        password = "sbkbgnedorcmuwyl"
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
                form(data)
                return JsonResponse({'status': 'success', 'message': "Re-enter the OTP"})
            
            
            else:
                try:
                    return JsonResponse({'status': 'error', 'message': "Re-enter the OTP"})
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': str(e)})
                
@csrf_exempt
def form(request):
    
    global otp
    if request.method=="POST":
            data = json.loads(request.body)
            
            print(data['otp'])
            print(otp,"global")
            form_class=Form()
            print(data)
            if str(otp)==str(data['otp']):
                name=data['name']
                fname=data['fname']
                phone=data['phone']
                email=data['email']
                address=data['address']
                dob=data['dob']
                age=data['age']
                cities=data['cities']
                nominee=data['nominee']
                dobnominee=data['dobnominee']
                agenominee=data['agenominee']
                nomineeRelation=data['nomineeRelation']
                mincome=data['mincome']
                suminsured=data['suminsured']
                term=data['term']
                premium=data['premium']
                mode=data['mode']
                disease=data['disease']
                operation=data['operation']
                yesno=data['yesno']
                habit=data['habit']
                Dfam=data['Dfam']
                Medexam=data['Medexam']
                height=data['height']
                weight=data['weight']
                chest=data['chest']
                abdomen=data['abdomen']
                suicide=data['suicide']
                falive=data['falive']
                malive=data['malive']
                fhealth=data['fhealth']
                fcd=data['fcd']
                mname=data['mname']
                mhealth=data['mhealth']
                # operation=data['operation']
                # premium=data['premium']
                mcd=data['mcd']
                numb=data['numb']
                nums=data['nums']
                
                Nos=data['Nos']
                Nod=data['Nod']
               

                
                form_class.Nos=Nos
                form_class.nums=nums
                form_class.Nod=Nod
                # form_class.files=files
                
                form_class.numb=numb
                form_class.mcd=mcd
                form_class.mhealth=mhealth
                form_class.causefdeath=fcd
                form_class.mothername=mname
                form_class.name=name
                form_class.father_name=fname
                form_class.phone=phone
                form_class.email=email
                form_class.address=address
                form_class.dob=dob
                form_class.age=age
                form_class.cities=cities
                form_class.nominee=nominee
                form_class.dob_nominee=dobnominee
                form_class.age_nominee=agenominee
                form_class.nominee_relation=nomineeRelation
                form_class.mincome=mincome
                form_class.suminsured=suminsured
                form_class.term=term
                form_class.premium=premium
                form_class.mode=mode
                form_class.disease=disease
                form_class.operation=operation
                form_class.yesno=yesno
                form_class.habit=habit
                form_class.Dfam=Dfam
                form_class.Medexam=Medexam
                form_class.height=height
                form_class.weight=weight
                form_class.chest=chest
                form_class.abdomen=abdomen
                form_class.suicide=suicide
                form_class.falive=falive
                form_class.malive=malive
                form_class.fhealth=fhealth
                
                
                # form_class.operation=operation
                # form_class.premium=premium
                
                
                
                
                # form_class.dob='2020-03-02'
                
                print(name,fname)
                form_class.save()
                return JsonResponse({'status': 'success', 'message': "Re-enter the OTP"})
            
            
            else:
                try:
                    return JsonResponse({'status': 'error', 'message': "Re-enter the OTP"})
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': str(e)})
        
    else:
        return render(request,"form.html",{})            
       
    
        
        
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
        team_email = request.POST.get('emailteam')
        if "@teams.com" in team_email:
            team_name = request.POST.get('teamname')
            team_pas = request.POST.get('teampass')
            if len(team_pas)>=5:
                created=team_register.objects.filter(team_email=team_email).exists()
                if created:
                    messages.error(request,"Email already exists!")
                    return redirect('target')
                else:
                    teams=team_register()
                    teams.team_name=team_name
                    teams.team_email=team_email
                    teams.team_password=team_pas
                    teams.save()
                    messages.error(request,"Team email already exist registered")
                    return redirect('target')
            else:
                messages.error(request,"length of password is not matched")
                return redirect('target')
        else:
            messages.error(request,"team email is not valid")
            return redirect('target')    
        
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

