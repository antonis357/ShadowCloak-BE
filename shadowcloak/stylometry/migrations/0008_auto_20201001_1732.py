# Generated by Django 3.1.1 on 2020-10-01 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stylometry', '0007_auto_20201001_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stylometry.author'),
            preserve_default=False,
        ),
    ]
