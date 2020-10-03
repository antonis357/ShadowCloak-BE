# Generated by Django 3.1.1 on 2020-10-03 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stylometry', '0016_group_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='author',
            field=models.ForeignKey(default=20, on_delete=django.db.models.deletion.CASCADE, to='stylometry.author'),
            preserve_default=False,
        ),
    ]