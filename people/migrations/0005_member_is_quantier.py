# Generated by Django 2.2.7 on 2019-12-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_member_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_quantier',
            field=models.BooleanField(default=False),
        ),
    ]
