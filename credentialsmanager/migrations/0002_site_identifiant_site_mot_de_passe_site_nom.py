# Generated by Django 4.2.9 on 2024-01-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentialsmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='identifiant',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='site',
            name='mot_de_passe',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='site',
            name='nom',
            field=models.CharField(default='', max_length=255),
        ),
    ]
