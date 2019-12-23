# Generated by Django 2.2.7 on 2019-12-19 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matirbank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matirbank',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='matirbank',
            name='bank_code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]