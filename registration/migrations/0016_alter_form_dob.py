# Generated by Django 4.0.1 on 2023-01-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_form_dfam_form_medexam_form_nod_form_nos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='dob',
            field=models.DateField(blank=True, default='2001-01-22', null=True),
        ),
    ]
