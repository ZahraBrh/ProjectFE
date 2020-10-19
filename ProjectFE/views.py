from django.http import HttpResponse, Http404,response
from django.shortcuts import redirect, render, reverse
from django.conf.urls import url 
from django.urls import path 
from django.contrib.auth.decorators import login_required 
from django.views.generic import TemplateView
from django.contrib.auth import logout
from accounts.models import Profile 
from articl.models import ArticlPub
from django.contrib.auth.models import User
from home.models import Follower
from articl.recommender import get_predict_list,demographic
from articl.views import detail_articl


def logout_view(request):
    logout(request)

    return redirect('login')



    

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