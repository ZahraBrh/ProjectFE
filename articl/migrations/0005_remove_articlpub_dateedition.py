# Generated by Django 3.0.8 on 2020-07-17 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articl', '0004_auto_20200717_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlpub',
            name='dateEdition',
        ),
    ]
