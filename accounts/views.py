from django.http import HttpResponse, Http404,response
from django.shortcuts import redirect, render, reverse
from django.conf.urls import url 
from django.urls import path 
from datetime import datetime
from django.contrib.auth import login, authenticate
from .forms import DetailsForm , CreateUserForm ,EditProfileForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

# Create your views here.

def index(request): 
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username ='not logged in'    

    context = {'username':username}    
    return render(request, 'accounts/index.html', context)

@login_required
def ProfileView(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}

    return render(request,'profile.html', args)



def registerPage(request):

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        profile_form = DetailsForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            #user.save_m2m() #maybe this is the error

            profile = profile_form.save(commit=False)
            profile.user=user

            user.labo_affiliation = profile_form.cleaned_data.get('labo_affiliation')
            user.domaine = profile_form.cleaned_data.get('domaine')
            user.location = profile_form.cleaned_data.get('location')
            user.birth_date = profile_form.cleaned_data.get('birth_date')
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)

            print('user created')
            messages.add_message(request, messages.SUCCESS , "You have Registered successfully" )
            return redirect('index')
    else:
        form=CreateUserForm()
        profile_form = DetailsForm()
            
            
            
    context = {'form' : form, 'profile_form' : profile_form }
    return render(request, 'accounts/register.html', context)  



def DetailsPage(request):
    
    if request.method == 'POST':
        myModelform = DetailsForm(request.POST)
        
        if myModelform.is_valid():    
            user=myModelform.save(commit=False)
            #user.user=myModelform.cleaned_data.get('user')
            user.first_name = myModelform.cleaned_data.get('first_name')
            user.last_name = myModelform.cleaned_data.get('last_name')
            user.birth_date = myModelform.cleaned_data.get('birth_date')
            user.email = myModelform.cleaned_data.get('email')
            user.password = myModelform.cleaned_data.get('password')
            user.labo_affiliation = myModelform.cleaned_data.get('labo_affiliation')
            user.domaine = myModelform.cleaned_data.get('domaine')
            user.location = myModelform.cleaned_data.get('location')
            
            myModelform.save()
            messages.add_message(request, messages.SUCCESS , "You have Registered successfully" )

            print('Profile Created')
    else:
        myModelform=DetailsForm(request.POST)

    context={'Modelform':DetailsForm}        
        
    return render(request, 'accounts/details.html', context)
         

def loginPage(request):

    context={}
    return render(request,'accounts/login.html',context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        
        context = {'form': form}
        return render(request, 'accounts/edit_profile.html', context)

