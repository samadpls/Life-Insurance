from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from registration.models import *

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json
import uuid
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage


# Create your views here.
login_id = ""


@csrf_exempt
def login(request):
    global login_id
    if request.method == 'GET':
        try:
            login_email = request.GET.get("login_name")
            login_pwd = request.GET.get("login_pwd")
            if "@teams.com" in login_email:
                try:
                    team = team_register.objects.get(
                        team_email=login_email, team_password=login_pwd)
                    return redirect("target")
                except team_register.DoesNotExist:
                    messages.error(request, "Email or password is not correct")
                    return redirect('login')
            elif "@salesmanager.com" in login_email:
                pass

            else:
                try:
                    client = register.objects.get(
                        user_name=login_email, user_password=login_pwd)
                    login_id = client.user_id
                    print(login_id, "index mai bhij raha ho")
                    # login wala page
                    return render(request, 'indexlogin.html', {})
                except register.DoesNotExist:
                    messages.error(request, "Email or password is not correct")
                    return redirect('login')

        except:
            return render(request, "login.html")

    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        if not (("@teams.com" or "@salesmanager.com") in email):
            cpwd = request.POST.get('cpassword')
            reg_id = register.objects.all()
            for id in reg_id:
                if id.user_name == email:
                    messages.error(request, "Email already exists")
                    return redirect('login')

            if pwd == cpwd:
                data = register()
                data.user_name = email
                data.user_password = pwd
                data.save()

            else:
                messages.error(request, "Password doesn't match")
                return redirect('login')

        else:
            messages.error(request, "Invalid Email")
            return redirect('login')

    return render(request, 'login.html', {})


def home(request):

    return render(request, 'index.html', {})


otp = ""


@csrf_exempt
def send_otp(request):
    global otp
    if request.method == "POST":
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


def handle_uploaded_file(f):  
    with open('/media/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)
            

@csrf_exempt
def form(request):
    global otp
    global login_id
    if request.method == "POST":

        form_class = Form()

        # print("FAIZAN", request.FILES)

        if str(request.POST.get('OTP')) == str(request.POST.get("OTP")):
            file=request.FILES.get('file')
            # handle_uploaded_file(file)
            fss = FileSystemStorage()
            file = fss.save("abc.jpg", file)
            file_url = fss.url(file)
            print("file_url", file_url)
            
            form_class.file=file

            form_class.OTP = request.POST.get("OTP")
            form_class.name = request.POST.get('cname')
            form_class.father_name = request.POST.get('cfname')
            form_class.phone = request.POST.get('phone')
            form_class.email = request.POST.get('email')
            form_class.address = request.POST.get('address')
            form_class.dob = request.POST.get('dob')
            form_class.age = request.POST.get('age')
            form_class.cities = request.POST.get('cities')
            form_class.nominee = request.POST.get('nominee')
            form_class.dob_nominee = request.POST.get('dobNominee')
            form_class.age_nominee = request.POST.get('ageNominee')
            form_class.nominee_relation = request.POST.get('nomineeRelation')
            form_class.mincome = request.POST.get('monthly-income')
            form_class.suminsured = request.POST.get('Sum-insured')
            form_class.term = request.POST.get('Term')
            # form_class.=request.POST.get('radioGroup')
            form_class.premium = request.POST.get('premium')
            form_class.disease = request.POST.get('disease')
            form_class.operation = request.POST.get('operation')
            form_class.yesno = request.POST.get('yesno')
            form_class.habit = request.POST.get('Tabacoo')
            # form_class.=request.POST.get('yesno1')
            form_class.Medexam = request.POST.get('med_examined')
            form_class.height = request.POST.get('height')
            form_class.weight = request.POST.get('weight')
            form_class.chest = request.POST.get('chest')
            form_class.abdomen = request.POST.get('abdomen')
            form_class.suicide = request.POST.get('suicide')
            form_class.father_name = request.POST.get('father')
            form_class.fhealth = request.POST.get('father-health')
            form_class.causefdeath = request.POST.get('fcd')
            form_class.mothername = request.POST.get('mother-name')
            form_class.malive = request.POST.get('mother-health')
            form_class.mcd = request.POST.get('mcd')
            form_class.numb = request.POST.get('numb')
            form_class.nums = request.POST.get('nums')
            form_class.Nod = request.POST.get('Nod')
            form_class.Nos = request.POST.get('Nos')
            form_class.mothername = request.POST.get('mother')

            form_class.save()

            return JsonResponse({'status': 'success', 'message': "Re-enter the OTP"})

        else:
            try:
                return JsonResponse({'status': 'error', 'message': "Re-enter the OTP"})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

    else:
        print("login_id", login_id)
        agents = team_register.objects.all()
        return render(request, 'form.html', {"agents": agents})


def signout(request):
    return redirect('/')


@csrf_exempt
def payPremium(request):
    if request.method == "POST":
        form_class = payPrem()

        # print("FAIZAN", request.FILES)

        file=request.FILES.get('file')
            # handle_uploaded_file(file)
        fss = FileSystemStorage()
        file = fss.save("abc.jpg", file)
        file_url = fss.url(file)
        print("file_url", file_url)
            
        form_class.file=file
        form_class.save()
        
        

    # form=Form.objects.get(id=34)
    # print(form.file)
    return render(request, 'payPremium.html')


def notification(request):

    clients = Form.objects.all()
    color = ["alert-primary", "alert-success", "alert-info",
             "alert-warning", "alert-danger", "alert-success", "alert-secondary"]

    return render(request, 'Notification.html', {"clients": clients, "color": color})


def RiskAssessment(request, id):
    clients = Form.objects.filter(id=id)
    context = {"clients": clients, "id": id}
    return render(request, 'RiskAssessment.html', context)


@csrf_exempt
def delete_item(request, team_id):

    data = team_register.objects.get(team_id=team_id)
    data.delete()

    return redirect('/target')


@csrf_exempt
def target(request):
    if request.method == 'POST':
        team_email = request.POST.get('emailteam')
        if "@teams.com" in team_email:
            team_name = request.POST.get('teamname')
            team_pas = request.POST.get('teampass')
            if len(team_pas) >= 5:
                created = team_register.objects.filter(
                    team_email=team_email).exists()
                if created:
                    messages.error(request, "Email already exists!")
                    return redirect('target')
                else:
                    teams = team_register()
                    teams.team_name = team_name
                    teams.team_email = team_email
                    teams.team_password = team_pas
                    teams.save()
                    messages.error(
                        request, "Team email already exist registered")
                    return redirect('target')
            else:
                messages.error(request, "length of password is not matched")
                return redirect('target')
        else:
            messages.error(request, "team email is not valid")
            return redirect('target')

    task = team_register.objects.all()

    print(task)
    # task2={'task':task}

    return render(request, "target.html", {'task': task})


def jevansaathi(request):
    return render(request, 'jevansaathi.html', {})


def WholeLifeAssurance(request):
    return render(request, 'WholeLifeAssurance.html', {})


def Sadabahar(request):
    return render(request, 'Sadabahar.html', {})


def ChildProtection(request):
    return render(request, 'ChildProtection.html', {})


def onlogin(request):
    global login_id
    return render(request, 'indexlogin.html', {"login_id": login_id})
