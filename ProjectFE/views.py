from django.http import HttpResponse, Http404,response
from django.shortcuts import redirect, render, reverse
from django.conf.urls import url 
from django.urls import path 
from django.contrib.auth.decorators import login_required 
from django.views.generic import TemplateView
from django.contrib.auth import logout

def logout_view(request):
    logout(request)

    return redirect('login')

    

