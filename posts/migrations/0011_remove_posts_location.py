# Generated by Django 2.0.3 on 2018-04-07 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_posts_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='location',
        ),
    ]
