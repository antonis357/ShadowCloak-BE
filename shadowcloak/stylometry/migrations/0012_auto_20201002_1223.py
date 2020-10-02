# Generated by Django 3.1.1 on 2020-10-02 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stylometry', '0011_auto_20201002_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60)),
                ('description', models.CharField(blank=True, max_length=240)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='stylometry.documentgroup'),
        ),
    ]