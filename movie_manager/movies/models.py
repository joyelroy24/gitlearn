from django.db import models

# Create your models here.


class Director(models.Model):
    name=models.CharField(max_length=100)
    certified_by=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name




class Actorinfo(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Movieinfo(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/',null=True)
    directed_by=models.ForeignKey(Director,null=True,on_delete=models.CASCADE,related_name='director')
    actor=models.ManyToManyField(Actorinfo,related_name='movie_actor')



    def __str__(self):
        return (str(self.id)+self.title)

class Censor0info(models.Model):
    rating=models.CharField(max_length=10,null=True)
    movie_detail=models.OneToOneField(Movieinfo,on_delete=models.SET_NULL,related_name='censor',null=True)
    



