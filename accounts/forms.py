from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.forms import ModelForm
from datetime import date


class CreateUserForm(UserCreationForm):
        email = forms.EmailField(required=True, help_text='Required.',widget=forms.EmailInput(attrs={'class':'form-control',
                          'placeholder':'Email...'}))
        first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                          'placeholder':'First name...'}))
        last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                          'placeholder':'Last name...'}))
        username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                          'placeholder':'Username...'}))
        class Meta:
            model = User
            fields = ['username','first_name','last_name','email','password1','password2',]
            
        def save(self,commit=True):
            user=super().save(commit=False)

            user.email=self.cleaned_data['email']
            user.first_name=self.cleaned_data['first_name']
            user.last_name=self.cleaned_data['last_name']

            if commit: 
                user.save()
            return user    


class DateInput(forms.DateInput):
    input_type='date'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class DetailsForm(ModelForm):

    #confirmation_mail = forms.EmailField(label="Mail de confirmation")
    
    #birth_date = forms.DateTimeField(widget=forms.DateInput())
    class Meta:
        model = Profile
        fields = ['birth_date','labo_affiliation','domaine','location','grade',]
        
        labels = {
            'labo_affiliation':'Affiliation',
            'domaine':'Field ',
        }
                                        
        widgets = {            
                        'labo_affiliation':forms.TextInput(attrs={'class':'form-control',
                                    'placeholder':'Affiliation...'}),

                        'domaine':forms.Select(attrs={'class':'form-control',
                                    'placeholder':'Select your field , domaine ...'}),
                        'grade':forms.Select(attrs={'class':'form-control',
                                    'placeholder':'Select your grade...'}),
                        'birth_date':forms.TextInput(attrs={'class':'form-control',
                                    'placeholder':'YYYY-MM-DD.'}),
                    }
        

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField( widget=forms.PasswordInput)


class EditProfileForm(UserChangeForm):
    class Meta:
            model = User
            fields = ['first_name','last_name','email','password']
            


