# Generated by Django 4.0.3 on 2022-05-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetclinic', '0008_animal_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='customSpecies',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
