# Generated by Django 3.0.7 on 2020-08-15 02:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articl', '0010_favorite_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlpub',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
