# Generated by Django 3.0.8 on 2020-07-10 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('grade', models.CharField(blank=True, max_length=100)),
                ('labo_affiliation', models.CharField(blank=True, max_length=100)),
                ('domaine', models.CharField(choices=[('1', 'Computer Hardware'), ('2', 'Computer Networking'), ('3', 'Computer Software'), ('4', 'Cloud computing'), ('5', 'Cyber Security and Ethical Hacking'), ('6', 'Data Science and Data Analysis'), ('7', 'Programming Language'), ('8', 'Artificial intelligence'), ('9', 'Operating system'), ('10', 'Web Development'), ('11', 'Web Designing'), ('12', 'Graphics design'), ('13', 'Network Analytics and testing'), ('14', 'Robotics'), ('15', 'others field')], default='Computer Software ', max_length=100)),
                ('numTel', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]