# Generated by Django 3.0.2 on 2020-01-29 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.FileField(upload_to='pic/'),
        ),
    ]