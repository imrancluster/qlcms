# Generated by Django 2.2.7 on 2019-12-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20191208_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]