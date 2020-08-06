import django_filters
import .models import Profile

class UserFilter(django_filters.FilterSet):
    class Meta:
                model = User
                fields = ['username','first_name','last_name']
