from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('form',form,name='form'),
    path('notification',notification,name='Risk Assessment notification page'),
    path('RiskAssessment',RiskAssessment,name='RiskAssessment'),
    path('payPremium',payPremium,name='payPremium')
]
