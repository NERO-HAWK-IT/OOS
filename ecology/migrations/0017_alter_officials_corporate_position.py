# Generated by Django 5.0 on 2024-01-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecology', '0016_alter_waste_collection_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officials',
            name='corporate_position',
            field=models.CharField(choices=[('Р', 'Руководитель'), ('З', 'Заместитель')], default='Р', max_length=12, verbose_name='Руководитель / Заместитель'),
        ),
    ]