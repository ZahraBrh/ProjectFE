from django.conf.urls import url
from . import views 
from django.urls import path
from django.views.generic import ListView
from .models import ArticlPub

app_name = 'articl'

urlpatterns = [
    #path(r'', views.index, name='index'),
    path('postarticl/',views.createPost,name='postarticl'),
    path('listarticl/',views.listArticl,name='listArticl'),
    path('recommendation/',views.recommandation,name='recommandation'),
    path('<int:pk>/', views.deleteArticl,name='delele_Articl'),
    url(r'^detail/(?P<pk>\d+)/$',views.detail_articl, name='detail_articl'),
    url(r'(?P<pk>\d+)/Favourite/$',views.favourite, name='favourite'),
    path('favourites/',views.favourite_list,name='favourite_list'),
    path('<int:pk>/', views.moyenne,name='moyenne'),
    path('ajouterNote/<int:pk>/',views.ajouter_Note, name="ajouter_note"),
    path('livres_note/', views.list_note, name='list_note'),
    
    
    #path('search/',views.SearchResults, name='search_results'),
    #path('search/',views.Articl_Filtred_list, name='search'),
    #path('class/articl/', views.ArticlListView.as_view(),name='class_articlList'),


]