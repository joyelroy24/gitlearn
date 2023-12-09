from django.db import models

# Create your models here.
class Movieinfo(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/',null=True)

class Director(models.Model):
    name=models.CharField(max_length=100)


