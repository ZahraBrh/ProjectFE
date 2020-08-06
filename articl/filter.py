import django_filters
from .models import ArticlPub

class PostFilter(django_filters.FilterSet):
    class Meta:
                model = ArticlPub
                fields = ['titre','keywords','resumé']
