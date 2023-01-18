from django.contrib import admin


from registration.models import register


class registeradmin(admin.ModelAdmin):
    lis=('user_id','user_name','user_password')
    
    
admin.site.register(register,registeradmin)

# Register your models here.
