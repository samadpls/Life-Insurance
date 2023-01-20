from django.contrib import admin


from registration.models import *


class registeradmin(admin.ModelAdmin):
    lis=('user_id','user_name','user_password')
    
    

    
    
admin.site.register(register,registeradmin)
admin.site.register(team_register)
admin.site.register(Form)

# Register your models here.
