from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('form', form, name='form'),
    path('notification', notification, name='Risk Assessment notification page'),
    path('RiskAssessment/<int:id>/', RiskAssessment, name='RiskAssessment'),
    path('update_record',update_record,name='update_record'),
    path("team",team,name="team"),
    path("target", target, name="target"),
    path('delete/<str:team_id>/', delete_item, name="delete"),
    path('delete_form/<int:id>/',delete_form,name="delete_form"),
    path('passed/<int:id>/',Passed,name="Passed"),
    path('send-otp', send_otp, name='send_otp'),
    path('payPremium', payPremium, name='payPremium'),
    path('signout', signout, name='signout'),

    path('login', login, name='login'),
    path("jevansaathi", jevansaathi, name='jevansaathi'),
    path("WholeLifeAssurance", WholeLifeAssurance, name='WholeLifeAssurance'),
    path("loggedin", onlogin, name="loggedin"),
    path("Sadabahar", Sadabahar, name='Sadabahar'),
    path("ChildProtection", ChildProtection, name='ChildProtection')

]



