# Generated by Django 5.0.1 on 2024-02-09 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='user_objects',
            new_name='user_object',
        ),
    ]
