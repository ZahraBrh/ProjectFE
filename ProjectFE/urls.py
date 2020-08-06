"""ProjectFE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve 
from django.conf.urls import url 
from accounts import views as accounts_views
from articl import views as articl_views

from ProjectFE import views
from home.views import HomeView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', HomeView.as_view(),name='home'),
    
    path(r'accounts/', include('accounts.urls', namespace='accounts' )),
    path(r'articl/', include('articl.urls', namespace='articl')),
    path(r'home/', include('home.urls', namespace='home')),
    
    path('register/', accounts_views.registerPage, name="register"),
    path(r'accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(),name='login'),
    #path('profile/',accounts_views.ProfileView, name='profile'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),
        ]

    