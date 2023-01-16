from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login',login,name='login'),
    path("jevansaathi",jevansaathi,name='jevansaathi'),
    path("WholeLifeAssurance",WholeLifeAssurance,name='WholeLifeAssurance'),
    path("Sadabahar",Sadabahar,name='Sadabahar'),
    path("ChildProtection",ChildProtection,name='ChildProtection')
    
]
