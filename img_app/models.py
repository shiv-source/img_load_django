from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    img = models.FileField(upload_to='pic/')
    video = models.FileField(upload_to='video/',default=True)

    def __str__(self):
        return self.name