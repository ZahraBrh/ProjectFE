# Generated by Django 3.0.8 on 2020-07-29 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articl', '0005_remove_articlpub_dateedition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlpub',
            name='published_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='articlpub',
            name='resumé',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='articlpub',
            name='titre',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='articlpub',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
