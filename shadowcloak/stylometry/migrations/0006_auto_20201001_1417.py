# Generated by Django 3.1.1 on 2020-10-01 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stylometry', '0005_remove_author_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=240, unique=True),
        ),
    ]
