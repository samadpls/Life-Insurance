# Generated by Django 4.0.1 on 2023-01-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0023_alter_form_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='file',
            field=models.FileField(default='', upload_to='media/'),
        ),
    ]
