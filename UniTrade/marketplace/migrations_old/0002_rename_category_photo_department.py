# Generated by Django 5.0.3 on 2024-04-04 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='category',
            new_name='department',
        ),
    ]