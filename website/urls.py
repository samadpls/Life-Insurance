from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('form',form,name='form'),
    path('notification',notification,name='Risk Assessment notification page'),
    path('RiskAssessment',RiskAssessment,name='RiskAssessment'),
    path('send-otp', send_otp, name='send_otp'),
    path('checkOTP', checkOTP, name='checkOTP'),
    path('payPremium',payPremium,name='payPremium'),
    path('login',login,name='login'),
    path("jevansaathi",jevansaathi,name='jevansaathi'),
    path("WholeLifeAssurance",WholeLifeAssurance,name='WholeLifeAssurance'),
    path("Sadabahar",Sadabahar,name='Sadabahar'),
    path("ChildProtection",ChildProtection,name='ChildProtection'),

]
