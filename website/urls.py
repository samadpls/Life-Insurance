from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('form',form,name='form'),
    path('notificatin',notification,name='Risk Assessment notification page'),
    path('RiskAssessment',RiskAssessment,name='Risk Assessment')
]
