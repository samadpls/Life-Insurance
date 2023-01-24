from django.db import models
import uuid
import datetime


class register(models.Model):
    user_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name=models.CharField(max_length=20)
    user_password=models.CharField(max_length=10)

class team_register(models.Model):
    team_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team_name=models.CharField(max_length=10)
    team_email=models.CharField(max_length=20)
    team_password=models.CharField(max_length=10)

class TeamProgress(models.Model):
    id_p = models.CharField(primary_key=True,max_length=100)
    team_progress = models.CharField(max_length=20,default=0)
    target_sales = models.CharField(max_length=20,default=0)
    target_sales_history = models.TextField(default='[]')

    
class Form(models.Model):
    date=  models.CharField(default=datetime.date.today(),max_length=200)
    passed=models.BooleanField(default=False)
    name = models.CharField(max_length=200 ,blank=True)
    father_name = models.CharField(max_length=200 ,blank=True)
    phone = models.CharField(max_length=20,blank=True )
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255,blank=True )
    dob = models.DateField(blank=True  ,default='2001-01-22',null=True)
    age = models.CharField(max_length=255,blank=True ,null=True)
    cities = models.CharField(max_length=255,blank=True ,null=True)
    nominee = models.CharField(max_length=255,default='2001-01-22', blank=True, null=True)
    dob_nominee = models.DateField(blank=True, null=True)
    age_nominee = models.PositiveIntegerField(blank=True, null=True)
    nominee_relation = models.CharField(max_length=255, blank=True, null=True)
    suminsured = models.CharField(max_length=20,default='500000',blank=True )
    term=models.CharField(max_length=20,blank=True)
    agentID=models.CharField(max_length=200,blank=True)

    PLANS = [
        ('Jeevan Sathi Assurance', 'Jeevan Sathi Assurance'),
        ('Child Protection Assurance', 'Child Protection Assurance'),
        ('Wealth Builder Plan', 'Wealth Builder Plan'),
        ('Supplementary Covers', 'Supplementary Covers'),
    ]
    plan = models.CharField(max_length=200, choices=PLANS, default='other')
    mincome = models.CharField(max_length=20,blank=True ,null=True)
    file=models.FileField(upload_to='media/',default="",null=True)
    # files = models.FileField(upload_to='document/')
    premium=models.CharField(max_length=20,blank=True,null=True)
    
    Mode = [
        ('yly', 'YLY'),
        ('hly', 'HLY'),
        ('qly', 'QLY')
    ]
    mode = models.CharField(max_length=200, choices=Mode, default='other',null=True)
    Disease = [
        ('cancer', 'Cancer'),
        ('diabetes', 'Diabetes'),
        ('heartDisease', 'Heart disease')
    ]
    disease = models.CharField(max_length=200, choices=Disease, default='other',null=True)
    
    Operation = [
        ('Appendectomy', 'Appendectomy'),
        ('openHeartSurgery', 'openHeartSurgery'),
        ('Hip replacement surgery', 'Hip replacement surgery')
    ]
    operation = models.CharField(max_length=200, choices=Operation, default='other',null=True)
    
    yesno = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    Weak_eye_sight  = models.CharField(max_length=200, choices=yesno, default='other')
    
    
    habit = [
        ('tabacoo', 'Tabacoo'),
        ('alcohal', 'Alcohal'),
        ('drugs', 'Drugs')
    ]
    habit = models.CharField(max_length=200, choices=habit, default='other',null=True)


    # Dfam = [
    #      ('yes', 'Yes'),
    #     ('no', 'No')
    # ]
    # Dfam = models.CharField(max_length=200, choices=Dfam, default='other')
    
    
    Medexam = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    Medexam = models.CharField(max_length=200, choices=Medexam, default='other',null=True)
    height=models.CharField(max_length=20,blank=True,null=True)

    weight=models.CharField(max_length=20,blank=True,null=True)

    chest=models.CharField(max_length=20,blank=True,null=True)

    abdomen=models.CharField(max_length=20,blank=True,null=True)
    
    suicide = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    suicide = models.CharField(max_length=200, choices=suicide, default='other',null=True)
    
    
    falive = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    falive = models.CharField(max_length=200, choices=falive, default='other',null=True)
    
    
    fhealth = [
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor',"Poor")
    ]
    fhealth = models.CharField(max_length=200, choices=fhealth, default='other',null=True)
    malive = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    malive = models.CharField(max_length=200, choices=malive, default='other',null=True)


    causefdeath = models.CharField(max_length=255,blank=True ,null=True)

    mothername= models.CharField(max_length=255,blank=True ,null=True)
    
    # mhealth = [
    #     ('good', 'Good'),
    #     ('fair', 'Fair'),
    #     ('poor',"Poor")
    # ]
    # mhealth = models.CharField(max_length=200, choices=mhealth, default='other')
    
    mcd = models.CharField(max_length=255,blank=True ,null=True)
    
    numb=models.CharField(max_length=20,blank=True,null=True)
    nums=models.CharField(max_length=20,blank=True,null=True)
    Nos=models.CharField(max_length=20,blank=True,null=True)
    Nod=models.CharField(max_length=20,blank=True,null=True)




    

    

    # cnic_bank_statement = models.FileField(upload_to='documents/', blank=True, null=True)
    # medical_report = models.FileField(upload_to='documents/', blank=True, null=True)
    
    # education = models.CharField(max_length=255, blank=True)
    # gpe_no = models.PositiveIntegerField(blank=True)
    # husbend_income = models.PositiveIntegerField(blank=True)
    # monthly_deduction = models.CharField(max_length=255, blank=True)
    # dol = models.DateField(blank=True)
    # yearly_deduction = models.CharField(max_length=255, blank=True)
    # DISEASE_CHOICES = [
    #     ('cancer', 'Cancer'),
    #     ('diabetes', 'Diabetes'),
    #     ('heartDisease', 'Heart disease'),
        
    #     ('other', 'Other'),
    # ]
    # disease = models.CharField(max_length=20, choices=DISEASE_CHOICES, default='other')
    # disease_description = models.TextField(blank=True, null=True)

    # OPERATION_CHOICES = [
    #     ('appendectomy', 'Appendectomy'),
    #     ('openHeartSurgery', 'Open heart surgery'),
    #     ('hipReplacementSurgery', 'Hip replacement surgery'),
    #     ('other', 'Other'),
    # ]
    # operation = models.CharField(max_length=200, choices=OPERATION_CHOICES, default='other')
    # operation_description = models.TextField(blank=True, null=True)
    # medically_examined = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    # height = models.FloatField()
    # weight = models.FloatField()
    # chest = models.FloatField()
    # abdomen = models.FloatField()
    # SUICIDE_CHOICES = [
    #     ('yes', 'Yes'),
    #     ('no', 'No'),
 