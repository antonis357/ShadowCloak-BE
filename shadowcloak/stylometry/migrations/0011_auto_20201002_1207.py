# Generated by Django 3.1.1 on 2020-10-02 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stylometry', '0010_document_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='group',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]
