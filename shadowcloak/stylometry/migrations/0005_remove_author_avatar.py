# Generated by Django 3.1.1 on 2020-09-28 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stylometry', '0004_author_pseudonym'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='avatar',
        ),
    ]
