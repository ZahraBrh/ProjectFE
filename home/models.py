from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    users = models.ManyToManyField(User,null=True,blank=True)
    current_user = models.ForeignKey(User, related_name='owener', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_follower(cls, current_user, new_follower):
        follower, created = cls.objects.get_or_create(current_user=current_user)
        follower.users.add(new_follower)

    @classmethod
    def lose_follower(cls, current_user, new_follower):
        follower, created = cls.objects.get_or_create(current_user=current_user)
        follower.users.remove(new_follower)