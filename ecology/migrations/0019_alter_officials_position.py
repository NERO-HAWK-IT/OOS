# Generated by Django 5.0 on 2024-01-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecology', '0018_alter_officials_corporate_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officials',
            name='position',
            field=models.CharField(max_length=70, verbose_name='Должность'),
        ),
    ]