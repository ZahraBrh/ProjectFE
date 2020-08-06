# Generated by Django 3.0.8 on 2020-07-29 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20200729_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owener', to=settings.AUTH_USER_MODEL),
        ),
    ]