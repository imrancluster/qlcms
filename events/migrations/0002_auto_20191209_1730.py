# Generated by Django 2.2.7 on 2019-12-09 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='publications',
            new_name='members',
        ),
    ]
