from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.views.generic import TemplateView, ListView , FormView
from .forms import Postform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.core.files.storage import FileSystemStorage
from .models import ArticlPub
from accounts import views

# Create your views here.
def index(request):
    return render(request ,'base.html')

@login_required
def createPost(request):

    if request.method == 'POST':    
        form = Postform(request.POST, request.FILES )
        if form.is_valid() :
            ArticlPub =form.save(commit=False)
            ArticlPub.user=request.user
            ArticlPub.titre=form.cleaned_data.get('titre')
            ArticlPub.resumé=form.cleaned_data.get('resumé')
            ArticlPub.keywords=form.cleaned_data.get('keywords')
            ArticlPub.maison_ed=form.cleaned_data.get('maison_ed')
            ArticlPub.typeArticl=form.cleaned_data.get('typeArticl')
            ArticlPub.published_date=form.cleaned_data.get('published_date')
            ArticlPub.path=form.cleaned_data.get('path')
            

            ArticlPub.save()
            form.save_m2m()

            print('post created')
            messages.add_message(request, messages.SUCCESS , "You have posted your articl successfully" )
            return redirect('index')
    else:
        form=Postform()        
        
    context = {'form':form}
    return render(request,"PostArticl.html",context)


@login_required
def deleteArticl(request, pk):
    if request.method == 'POST':
        articl=ArticlPub.objects.get(pk=pk)
        articl.delete()
    return redirect('listArticl')



@login_required
def listArticl(request):
    artPubs=ArticlPub.objects.all() 
    return render(request,'ListArticl.html',{'artPubs':artPubs})

class ArticlListView(ListView):
    model = ArticlPub
    template_name = 'article/listé.html'
    context_object_name = 'articlpubs'


    