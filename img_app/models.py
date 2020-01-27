from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pic/')

    def __str__(self):
        return self.name