from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.views.generic import TemplateView, ListView , FormView
from .forms import Postform,NoteForm,FaveForm
from django.contrib import messages
from django.db.models import F,Aggregate,Avg
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.core.files.storage import FileSystemStorage
from .models import ArticlPub,Note,Favorite
from accounts import views
from django.contrib.auth.models import User
from django.template.context import RequestContext

# Create your views here.
def index(request):
    return render(request ,'base.html')

@login_required
def detail_articl(request,pk):
    articl=ArticlPub.objects.get(pk=pk)
    notes=Note.objects.filter(articl=pk)
    average=notes.aggregate(Avg("note"))['note__avg']
    if average==None:
        average=0

    is_favourite=False
    if articl.favourite.filter(pk=request.user.pk).exists():
        is_favourite=True

    #is_rated=False
    #if Note.user.filter(articl=pk,pk=request.user.pk).exists():
     #  is_rated=True
     
    context={'articl':articl,
            'notes':notes,
            'average':average,
            'is_favourite':is_favourite,
            #'is_rated':is_rated
            }
    return render(request,'detailArticl.html',context)

@login_required
def favourite_list(request):
    user= request.user
    favourite_articls=user.favourite.all()
    context={
        'favourite_articls':favourite_articls
    }
    return render(request,'favourite_list.html',context)

@login_required
def createPost(request):
     # if not request.user.is_authenticated():
    #    raise Http404
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
def deleteArticl(request,pk):
    
    if request.method == 'POST':
        articl=ArticlPub.objects.get_or_create(pk=pk)
        articl.delete()
    return  redirect('articl:listArticl')

def add_f(request,pk):
    fav_art=ArticlPub.objects.get(pk=pk)    
    Favorite.add_favorite(request.user, new_favorite) 
    return redirect('ListArticl.html')

@login_required
def listArticl(request):
    
    artPubs=ArticlPub.objects.all().order_by("-timestamp")
    notes=Note.objects.all()
    context = {'artPubs':artPubs,'notes':notes}
    return render(request,"ListArticl.html",context)

def favourite(request,pk):
    articl=get_object_or_404(ArticlPub,pk=pk)
    if articl.favourite.filter(pk=request.user.pk).exists():
        articl.favourite.remove(request.user)
        print('remove to fav')
    else:
        articl.favourite.add(request.user)
        print('add to fav')

    #return HttpResponseRedirect(articl.get_absolute_url())
    return redirect('home:home')

@login_required
class ArticlListView(ListView):
    model = ArticlPub
    template_name = 'article/listé.html'
    context_object_name = 'articlpubs'

@login_required
def ajouter_Note(request, pk):

    articl = ArticlPub.objects.get(pk=pk)
    note=Note.objects.all()
    user=request.user.id
    if Note.objects.filter(user=user,articl=articl).exists():
        Note.objects.filter(user=user,articl=articl).delete()
        if request.method == "POST":
            form = NoteForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.note=request.POST["note"]
                data.user=request.user
                data.articl= articl
                data.save()
                print('note ajouter')
                return redirect('articl:listArticl')
        else:
            form = NoteForm()

    else:
    
        if request.method == "POST":
            form = NoteForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.note=request.POST["note"]
                data.user=request.user
                data.articl= articl
                data.save()
                print('note ajouter')
                return redirect('articl:listArticl')
        else:
            form = NoteForm()
    
        
         
    return render(request, 'ListArticl.html', {"form": form})



def saveInfos(request):
    user = User.objects.get(username=request.POST["user"])
    articl = ArticlPub.objects.get(id=request.POST["articl"])
    note = Note.objects.filter(user=user, articl=articl)
    if note:
        user_note = Note.objects.get(user=user, articl=articl)
        user_note.note = request.POST["note"]
        user_note.save()
    else:
        user_note = Note(articl=articl, user=user, note=request.POST["note"])
        user_note.save()


def list_note(request):
    notes = Note.objects.filter(user=request.user)
    if request.POST:
        saveInfos(request, request.POST["type"])

    context={
        'notes':notes
    }
    return render(request,'liste_note.html',context)

def ajouter_(request, pk):

    articl = ArticlPub.objects.get(pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.note=form.cleaned_data.get('note')
            data.user=request.user
            data.articl=articl
            data.save()
            print('note ajouter')
            return redirect('articl:listArticl')
    else:
        form = NoteForm()
    return render(request, 'ListArticl.html', {"form": form})



def moyenne(request,pk):
    if request.method == 'POST':
        notes=Note.objects.all().filter(articl=pk)
        average=Note.objects.all().aggregate(Avg("note"))['note__avg']
        print(average)
        context={}
        return render(request,'ListArticl.html',context)

    
def favorite(request,pk):
    user = User.objects.get(id=request.POST["user"])
    articl = ArticlPub.objects.get(id=request.POST["articl"])
    in_favorite=Favorite.objects.filter(user=user,articl=articl)
    if in_favorite:
        instance = Favoris.objects.get(user=user, livre=livre)
        instance.delete()
    else:
        instance = Favoris(livre=livre, user=user)
        instance.save()
    
    
       
    return render(request,'recommandation/list_favoris.html',context)


    
def add_favorite(request, pk):
    articl = ArticlPub.objects.get(pk=pk)
    user=request.user.id
    if Favorite.objects.filter(user=user,articl=articl).exists():
        Favorite.objects.filter(user=user,articl=articl).delete()
    else:
        if request.method == "POST":
            form = FaveForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.is_favorite=True
                data.user=request.user
                data.articl= articl
                data.save()
                print('note ajouter')
                return redirect('articl:listArticl')
        else:
            form = NoteForm()
    
    return render(request, 'ListArticl.html', {"form": form})
