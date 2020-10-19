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
from articl.recommender import get_predict_list,demographic
from articl.views import detail_articl


class HomeView(TemplateView):
    template_name = 'home.html'
    
    
    def get(self, request):
        profiles=Profile.objects.exclude(id=request.user.id)
        users = User.objects.exclude(id=request.user.id) 
        arts=ArticlPub.objects.all() 

        follower, created = Follower.objects.get_or_create(current_user=request.user)
        followers = follower.users.all()
        predict_list = get_predict_list(request.user)
        print(predict_list)
        #rec=User.objects.filter(pk__in=predict_list)
        #second start
        demographic_list = demographic(request.user)
        print(demographic_list)
        
        for item in demographic_list.keys():
            if item not in predict_list:
                predict_list.append(item)
        
        
        rec=User.objects.filter(pk__in=predict_list)

        articlList = []
        for value in predict_list:
            #art=ArticlPub.objects.filter(user=value)
            articlList.append(value)
        
        
        articls=ArticlPub.objects.filter(user__id__in=articlList) #get articles where user__id is __in the list articlList
        
        print(articlList) 
        #second end

        args = {'profiles':profiles,
        'arts':arts,
        'users':users,
        'followers':followers,
        'articls':articls,
        'rec':rec}
        return render(request, self.template_name, args)

@login_required
def avr_fav(request,pk):
    articl=ArticlPub.objects.get(pk=pk)
    notes=Note.objects.filter(articl=pk)
    average=notes.aggregate(Avg("note"))['note__avg']
    if average==None:
        average=0
    average=(round(average,2))

    is_favourite=False
    if articl.favourite.filter(pk=request.user.pk).exists():
        is_favourite=True

    context={
            'average':average,
            'is_favourite':is_favourite,
            }
    return render(request,'home:home',context)


@login_required
def change_followers(request, operation , pk):
    new_follower=User.objects.get(pk=pk)
    
    if operation == 'add':
        Follower.make_follower(request.user, new_follower) 
    elif operation == 'remove':
        Follower.lose_follower(request.user, new_follower)
      
    return redirect('home:home')

