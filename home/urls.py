from django.conf.urls import url
from . import views 
from django.urls import path
from .views import HomeView, change_followers

app_name = 'home'

urlpatterns = [
    path(r'', HomeView.as_view(),name='home'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',views.change_followers, name='change_followers'),
    path('<int:pk>/', views.avr_fav,name='avr_fav'),
]