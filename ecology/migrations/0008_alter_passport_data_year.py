# Generated by Django 5.0 on 2024-01-15 19:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecology', '0007_alter_passport_data_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport_data',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=2017, message='Год д.б. 4-х значным!')], verbose_name='Год данных'),
        ),
    ]