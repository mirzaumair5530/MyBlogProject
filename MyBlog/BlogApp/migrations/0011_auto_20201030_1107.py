# Generated by Django 3.0.8 on 2020-10-30 06:07

import BlogApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0010_auto_20201030_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(default=BlogApp.models.cid, max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
