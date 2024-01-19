# Generated by Django 5.0 on 2024-01-19 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecology', '0011_alter_danger_class_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structural_division',
            name='location_map',
            field=models.ImageField(upload_to='ecology/images/location_scheme/', verbose_name='Схема местоположения'),
        ),
        migrations.AlterField(
            model_name='waste_types',
            name='picture',
            field=models.ImageField(upload_to='ecology/images/waste_image/', verbose_name='Картинка отхода'),
        ),
    ]