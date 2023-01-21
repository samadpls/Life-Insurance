from django.db import models
import uuid


class register(models.Model):
    user_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name=models.CharField(max_length=20)
    user_password=models.CharField(max_length=10)

class team_register(models.Model):
    team_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team_name=models.CharField(max_length=10)
    team_email=models.CharField(max_length=20)
    team_password=models.CharField(max_length=10)
class Form(models.Model):
    
    name = models.CharField(max_length=200 ,blank=True)
    father_name = models.CharField(max_length=200 ,blank=True)
    phone = models.CharField(max_length=20,blank=True )
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255,blank=True )
    dob = models.DateField(blank=True  ,default='2001-01-22',null=True)
    age = models.CharField(max_length=255,blank=True )
    cities = models.CharField(max_length=255,blank=True )
    nominee = models.CharField(max_length=255,default='2001-01-22', blank=True, null=True)
    dob_nominee = models.DateField(blank=True, null=True)
    age_nominee = models.PositiveIntegerField(blank=True, null=True)
    nominee_relation = models.CharField(max_length=255, blank=True, null=True)
    mincome = models.CharField(max_length=20,blank=True )
    suminsured = models.CharField(max_length=20,blank=True )
    term=models.CharField(max_length=20,blank=True)
    # files = models.FileField(upload_to='document/')
    premium=models.CharField(max_length=20,blank=True)
    Mode = [
        ('yly', 'YLY'),
        ('hly', 'HLY'),
        ('qly', 'QLY')
    ]
    mode = models.CharField(max_length=200, choices=Mode, default='other')
    Disease = [
        ('cancer', 'Cancer'),
        ('diabetes', 'Diabetes'),
        ('heartDisease', 'Heart disease')
    ]
    disease = models.CharField(max_length=200, choices=Disease, default='other')
    
    Operation = [
        ('Appendectomy', 'Appendectomy'),
        ('openHeartSurgery', 'openHeartSurgery'),
        ('Hip replacement surgery', 'Hip replacement surgery')
    ]
    operation = models.CharField(max_length=200, choices=Operation, default='other')
    
    yesno = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    yesno = models.CharField(max_length=200, choices=yesno, default='other')
    
    
    habit = [
        ('tabacoo', 'Tabacoo'),
        ('alcohal', 'Alcohal'),
        ('drugs', 'Drugs')
    ]
    habit = models.CharField(max_length=200, choices=habit, default='other')


    Dfam = [
         ('yes', 'Yes'),
        ('no', 'No')
    ]
    Dfam = models.CharField(max_length=200, choices=Dfam, default='other')
    
    
    Medexam = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    Medexam = models.CharField(max_length=200, choices=Medexam, default='other')
    height=models.CharField(max_length=20,blank=True)

    weight=models.CharField(max_length=20,blank=True)

    chest=models.CharField(max_length=20,blank=True)

    abdomen=models.CharField(max_length=20,blank=True)
    
    suicide = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    suicide = models.CharField(max_length=200, choices=suicide, default='other')
    
    
    falive = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    falive = models.CharField(max_length=200, choices=falive, default='other')
    
    
    fhealth = [
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor',"Poor")
    ]
    fhealth = models.CharField(max_length=200, choices=fhealth, default='other')
    malive = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    malive = models.CharField(max_length=200, choices=malive, default='other')


    causefdeath = models.CharField(max_length=255,blank=True )

    mothername= models.CharField(max_length=255,blank=True )
    
    mhealth = [
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor',"Poor")
    ]
    mhealth = models.CharField(max_length=200, choices=mhealth, default='other')
    
    mcd = models.CharField(max_length=255,blank=True )
    
    numb=models.CharField(max_length=20,blank=True)
    nums=models.CharField(max_length=20,blank=True)
    Nos=models.CharField(max_length=20,blank=True)
    Nod=models.CharField(max_length=20,blank=True)




    

    

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
    # ]
    # HEALTH_CHOICES = [
    #     ('good', 'Good'),
    #     ('fair', 'Fair'),
    #     ('poor', 'Poor'),
    # ]

    # suicide = models.CharField(choices=SUICIDE_CHOICES, max_length=3)
    # father_alive = models.BooleanField(default=True)
    # father_name = models.CharField(max_length=100, blank=True)
    # father_health = models.CharField(choices=HEALTH_CHOICES, max_length=5, blank=True)
    # father_dob = models.DateField(blank=True)
    # father_cause_of_death = models.CharField(max_length=100, blank=True)
    # father_passed_away = models.DateField(blank=True)
    # mother_alive = models.BooleanField(default=True)
    # mother_name = models.CharField(max_length=100, blank=True)
    # mother_health = models.CharField(choices=HEALTH_CHOICES, max_length=5, blank=True)
    # mother_dob = models.DateField(blank=True)
    # mother_cause_of_death = models.CharField(max_length=100, blank=True)
    # mother_passed_away = models.DateField(blank=True)
    
# Create your models here.
