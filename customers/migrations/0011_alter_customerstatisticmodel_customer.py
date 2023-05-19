# Generated by Django 3.2.18 on 2023-04-29 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0010_customerstatisticmodel_fillfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerstatisticmodel',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistic', to=settings.AUTH_USER_MODEL, verbose_name="Customer's statistic"),
        ),
    ]
