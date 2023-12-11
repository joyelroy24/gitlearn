from django.db import models

# Create your models here.
class Movieinfo(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/',null=True)

class Director(models.Model):
    name=models.CharField(max_length=100)
    certified_by=models.CharField(max_length=200,null=True)


class Censorinfo(models.Model):
    rating=models.CharField(max_length=10,null=True)
    movie_detail=models.OneToOneField(Movieinfo,on_delete=models.SET_NULL,related_name='censor',null=True)
    



