from django.shortcuts import redirect, render,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse
import json
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request, 'index.html',{})
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
                return JsonResponse({'status': 'error', 'message': "Re-enter the OTP"})
            
            
            else:
                try:
                    return JsonResponse({'status': 'error', 'message': "Re-enter the OTP"})
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': str(e)})
                



            
    # return render(request,"form.html",{})

def form(request):
        # if request.method=="POST":
        #     data = json.loads(request.body)
        #     if otp==data['otp']:
        #         messages.success("Form succesfully sumbitted")
        #         try:
        #             return JsonResponse({'status': 'success'})
        #         except Exception as e:
        #             return JsonResponse({'status': 'error', 'message': str(e)})
        #     else:
        #         return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
        return render(request,"form.html")    

def notification(request):
    
    clients=['Jhon',"ali","umer","qasim"]
    color=["alert-primary","alert-success","alert-info","alert-warning","alert-danger","alert-success","alert-secondary"]

    
    return render(request, 'Notification.html',{"clients":clients,"color":color})   
    

def payPremium(request):
    return render(request, 'payPremium.html',{})    
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


# def verify_otp(request):
#     if request.otp == otp:
#         for()
#     else:
#         return False