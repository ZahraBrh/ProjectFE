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
    
    DOMAINE=(
        #list of fields https://www.quora.com/What-are-different-fields-in-computer-science
        ('1','Computer Hardware'),
        ('2','Computer Networking'),
        ('3','Computer Software'),
        ('4','Cloud computing'),
        ('5','Cyber Security and Ethical Hacking'),
        ('6','Data Science and Data Analysis'),
        ('7','Programming Language'),
        ('8','Artificial intelligence'), 
        ('9','Operating system'),
        ('10','Web Development'),
        ('11','Web Designing'),
        ('12','Graphics design'),
        ('13','Network Analytics and testing'),
        ('14','Robotics'),
        ('15','others field'),

        )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre=models.CharField(max_length=500)
    resumé=models.CharField(max_length=2000, blank=True)
    keywords=models.CharField(max_length=500, blank=True)
    maison_ed=models.CharField(max_length=500,blank=True)
    typeArticl=models.CharField(max_length=100,blank=False,choices=ArticlTYPE)
    #published_date = models.DateField(null=True, blank=True)
    path=models.FileField(blank=True,null=True,upload_to='chapter/%Y/')
    auteurEcrit = models.ManyToManyField(Profile, blank=True, null=True)
    favourite = models.ManyToManyField(User,related_name='favourite', blank=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    domaineArt=models.CharField(max_length=100,choices=DOMAINE,blank=False,default='Computer Software ')
    def __str__(self):
      return self.titre

    

    def delete(self, *args, **kwargs):
       self.path.delete()
       super().delete(*args, **kwargs)
    
    def get_avg_rating(self):
      notes = Note.objects.filter(articl=self)
      count = len(notes)
      if count == 0:
        return(0)
      
      sum = 0
      for nt in notes:
        sum += nt.note
      return (sum/count)


        
        
    


class Note(models.Model):
    note = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)
    articl = models.ForeignKey(ArticlPub, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.articl.titre
         




class Favorite(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    articl = models.ForeignKey(ArticlPub, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
      return self.articl.titre
    
    @classmethod
    def add_favorite(cls, current_user, new_fav):
        favorite, created = cls.objects.get_or_create(current_user=current_user)
        favorite.users.add(new_fav)
    


    #after any changes: python manage.py makemigrations //// python manage.py migrate