# Generated by Django 3.0.3 on 2020-03-02 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationuser',
            name='rated_user_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='applicationuser',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
