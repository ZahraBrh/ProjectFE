from django.http import HttpResponse, Http404,response
from django.shortcuts import redirect, render, reverse,get_object_or_404
from django.conf.urls import url 
from django.urls import path 
from django.contrib.auth.decorators import login_required 
from django.views.generic import TemplateView
from accounts.models import Profile 
from articl.models import ArticlPub
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Follower





class HomeView(TemplateView):
    template_name = 'home.html'
    
    
    def get(self, request):
        profiles=Profile.objects.exclude(id=request.user.id)
        users = User.objects.exclude(id=request.user.id) 
        arts=ArticlPub.objects.all() 
        
        follower, created = Follower.objects.get_or_create(current_user=request.user)
        followers = follower.users.all()
        

        args = {'profiles':profiles,'arts':arts,'users':users,'followers':followers}
        return render(request, self.template_name, args)






def change_followers(request, operation , pk):
    new_follower=User.objects.get(pk=pk)
    
    if operation == 'add':
        Follower.make_follower(request.user, new_follower) 
    elif operation == 'remove':
        Follower.lose_follower(request.user, new_follower)
      
    return redirect('home:home')

