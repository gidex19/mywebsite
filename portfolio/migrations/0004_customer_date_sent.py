# Generated by Django 2.2.2 on 2021-02-06 10:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210206_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_sent',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
