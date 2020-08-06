from django import forms
from .models import ArticlPub
from django.forms import ModelForm
from datetime import date



class Postform(forms.ModelForm):
    
    class Meta:
        model = ArticlPub
        fields = [
            "titre",
            "resumé",
            "keywords",
            "maison_ed",
            "typeArticl",
            "published_date",
            "path",
            "auteurEcrit",
        ]

        widgets = {
            "titre":forms.TextInput(attrs={'class':'form-control',
                                    'placeholder':'Title...'}),
            "resumé":forms.Textarea(attrs={'class':'form-control',
                                    'placeholder':'abstract...'}),   
            "keywords":forms.TextInput(attrs={'class':'form-control',
                                    'placeholder':'Keywords...'}),
            "typeArticl":forms.Select(attrs={'class':'form-control',
                                    'placeholder':'Select articl type...'}),
            "maison_ed":forms.TextInput(attrs={'class':'form-control',
                                    'placeholder':'publishing house...'}),
            "published_date":forms.DateInput(attrs={'class':'form-control',
                                    'placeholder':'YYYY-MM-DD'}),
            "auteurEcrit":forms.SelectMultiple(attrs={'class':'form-control',
                                    'placeholder':'Please select authors ...'}),
                    

                    }

"""class EcritForm(forms.ModelForm):
    class Meta:
        model = Ecrit
        fields = [
            "auteurEcrit",
            "articlEcrit",
            "ordreAuteur",
            ]"""

class SearchForm(forms.ModelForm):

    class Meta:
         model = ArticlPub
         fields = ['titre','keywords','resumé']