# Generated by Django 4.2.9 on 2024-01-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentialsmanager', '0002_site_identifiant_site_mot_de_passe_site_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='identifiant',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='site',
            name='mot_de_passe',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='site',
            name='nom',
            field=models.CharField(default='', max_length=200),
        ),
    ]