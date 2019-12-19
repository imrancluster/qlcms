# Generated by Django 2.2.7 on 2019-12-19 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geography', '0003_auto_20191123_2236'),
        ('people', '0005_member_is_quantier'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MatirBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_code', models.CharField(max_length=20)),
                ('family_code', models.CharField(blank=True, max_length=20, null=True)),
                ('distribution_date', models.DateField(blank=True, null=True)),
                ('collection_date', models.DateField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('status', models.CharField(blank=True, choices=[('DISTRIBUTED', 'DISTRIBUTED'), ('COLLECTED', 'COLLECTED'), ('MONEY_RECEIPT', 'MONEY_RECEIPT')], max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.Branch')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='people.Member')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
