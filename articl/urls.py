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

    path('<int:pk>/', views.deleteArticl,name='delele_Articl'),
    #path('search/',views.SearchResults, name='search_results'),
    #path('search/',views.Articl_Filtred_list, name='search'),
    #path('class/articl/', views.ArticlListView.as_view(),name='class_articlList'),


]