# Generated by Django 3.1.1 on 2020-10-06 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stylometry', '0017_auto_20201003_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='pseudonym',
            new_name='name',
        ),
    ]