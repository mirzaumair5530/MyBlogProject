# Generated by Django 3.0.8 on 2020-10-30 06:07

import BlogApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0009_auto_20201030_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.IntegerField(default=BlogApp.models.cid, primary_key=True, serialize=False, unique=True),
        ),
    ]