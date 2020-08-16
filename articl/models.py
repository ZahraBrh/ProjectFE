from django.db import models
from accounts.models import Profile
from django.utils import timezone
import os
from django.conf import settings
from django.contrib.auth.models import User

class ArticlPub(models.Model):
    ArticlTYPE=(
      ('1','Research Article'),
      ('2','Research Paper'),
      ('3','Review Paper'),
      ('4','Review Article'),
      ('5','Peer-Reviewed Articles'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre=models.CharField(max_length=500)
    resumé=models.CharField(max_length=1000, blank=True)
    keywords=models.CharField(max_length=500, blank=True)
    maison_ed=models.CharField(max_length=500,blank=True)
    typeArticl=models.CharField(max_length=100,blank=False,choices=ArticlTYPE)
    #published_date = models.DateField(null=True, blank=True)
    path=models.FileField(blank=True,null=True,upload_to='chapter/%Y/')
    auteurEcrit = models.ManyToManyField(Profile, blank=True, null=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
      return self.titre

    

    def delete(self, *args, **kwargs):
       self.path.delete()
       super().delete(*args, **kwargs)  
        
  #after any changes: python manage.py makemigrations //// python manage.py migrate  


class Note(models.Model):
    note = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)
    articl = models.ForeignKey(ArticlPub, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        u=self.articl.titre
        return u