# Generated by Django 3.0.8 on 2020-07-15 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articl', '0002_auto_20200715_0249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlpub',
            name='auteurs',
        ),
        migrations.AddField(
            model_name='articlpub',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Ecrit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordreAuteur', models.IntegerField()),
                ('articlEcrit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articl.ArticlPub')),
                ('auteurEcrit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]
