from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import LoginView 

app_name = 'accounts'

urlpatterns = [
    path(r'', views.index, name="index"),
    path('register/', views.registerPage, name="register"),
    path('register/Details/', views.DetailsPage, name="Details"),
    path('login/', LoginView.as_view()),
    path('profile/',views.ProfileView, name='profile'),
    url(r'^profile/(?P<pk>\d+)/$',views.ProfileView, name='profile_with_pk'),
    path('edit/',views.edit_profile, name='edit_profile'),

]