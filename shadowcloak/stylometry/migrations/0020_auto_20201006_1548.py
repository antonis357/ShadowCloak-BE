# Generated by Django 3.1.1 on 2020-10-06 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stylometry', '0019_auto_20201006_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name2',
            new_name='name',
        ),
    ]