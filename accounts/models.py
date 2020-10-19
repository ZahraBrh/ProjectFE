from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from multiselectfield import MultiSelectField



class Profile(models.Model):
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
    
    GRADE=(
            ('1','Category A '),
            ('2','Category B '),
            ('3','Category C '),
            ('4','Category D '),
            )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    grade=models.CharField(max_length=100,blank=True,choices=GRADE,default='Category D ')
    labo_affiliation=models.CharField(max_length=100,blank=True,)
    domaine=models.CharField(max_length=100,choices=DOMAINE,blank=False,default='Computer Software ')
    numTel=models.IntegerField(null=True,blank=True)
    #profile_photo=models.ImageField(blank=True,null=True,upload_to='profilePhotos')
    def __str__(self):
      return self.user.username 



  #after any changes: python manage.py makemigrations //// python manage.py migrate



