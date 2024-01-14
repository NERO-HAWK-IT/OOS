# Generated by Django 5.0 on 2024-01-14 10:39

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Марка автомобиля')),
                ('car_type', models.CharField(max_length=15, verbose_name='Тип автомоиля')),
                ('prod_year', models.DateField(verbose_name='Дата производства')),
                ('eco_class', models.CharField(max_length=5, verbose_name='Экологический класс')),
                ('start_date', models.DateField(verbose_name='Дата начала эксплуатации')),
                ('end_date', models.DateField(blank=True, verbose_name='Дата окончания эксплуатации')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='Company_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала использования данных')),
                ('company_name', models.CharField(max_length=100, verbose_name='Наименование юридического лица')),
                ('OKED', models.CharField(max_length=100, verbose_name='Вид деятельности по ОКЭД')),
                ('UNP', models.CharField(max_length=9, verbose_name='УНП')),
                ('UNP_date', models.DateField(verbose_name='Дата УНП')),
                ('OKPO', models.CharField(max_length=11, verbose_name='ОКПО')),
                ('num_subdiv', models.IntegerField(verbose_name='Количество структурных подразделений')),
                ('postal_address', models.CharField(max_length=255, verbose_name='Почтовый адресс')),
                ('legal_address', models.CharField(max_length=255, verbose_name='Юридический адресс')),
                ('e_mail', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Данные компании',
                'verbose_name_plural': 'Данные компании',
            },
        ),
        migrations.CreateModel(
            name='Danger_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='Код д.б. 2-ух значным!'), django.core.validators.MaxLengthValidator(limit_value=2, message='Код д.б. 2-ух значным!')], verbose_name='Код класса опасности')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Нименование класса')),
                ('short_name', models.CharField(max_length=10, verbose_name='Краткое наименование класса')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы опаснсоти',
            },
        ),
        migrations.CreateModel(
            name='Landfill_facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, verbose_name='Код объекта захоронения')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Наименование объекта захоронения')),
            ],
            options={
                'verbose_name': 'Объект захоронения',
                'verbose_name_plural': 'Объекты захоронения',
            },
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, verbose_name='Регистрационный номер документа')),
                ('start_date', models.DateField(verbose_name='Дата начала действия')),
                ('end_date', models.DateField(verbose_name='Дата окончания действия')),
                ('conditions', models.CharField(blank=True, max_length=255, verbose_name='Условия разрешения/лицензии')),
                ('permit_waste', models.DecimalField(decimal_places=5, max_digits=7, verbose_name='Количество отходов согласно разрешения (всего)')),
                ('waste_III', models.DecimalField(decimal_places=5, max_digits=7, verbose_name='Количество отходов III класса, согласно разрешения (всего)')),
            ],
            options={
                'verbose_name': 'Лицензия',
                'verbose_name_plural': 'Лицензии',
            },
        ),
        migrations.CreateModel(
            name='Passport_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(verbose_name='Год данных')),
                ('name', models.CharField(choices=[('Топливо', [('DISEL', 'Дизельное топливо'), ('PET92', 'Бензин АИ-92'), ('PET95', 'Бензин АИ-95'), ('PET98', 'Бензин АИ-98'), ('PET100', 'Бензин АИ-100')]), ('Энергоресурсы', [('EL', ''), ('HEAT', ''), ('WAT_S', ''), ('WAT_D', '')]), ('Деятельность', [('SOLD', 'Проданная продукция, единиц')]), ('Выплаты', [('TAX', 'Налог на захоронение'), ('FINE', 'Штрафы ООС')])], max_length=100, verbose_name='Наименование показателя')),
                ('unit', models.CharField(max_length=10, verbose_name='Единица измерения')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Значение показателя')),
            ],
            options={
                'verbose_name': 'Данные для паспорта',
                'verbose_name_plural': 'Данные для паспорта',
            },
        ),
        migrations.CreateModel(
            name='Reason_for_transferring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование причины')),
                ('code', models.CharField(max_length=2, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='Код д.б. 2-ух значным!'), django.core.validators.MaxLengthValidator(limit_value=2, message='Код д.б. 2-ух значным!')], verbose_name='Код причины')),
                ('short_name', models.CharField(max_length=10, verbose_name='Краткое наименование причины')),
            ],
            options={
                'verbose_name': 'Причина',
                'verbose_name_plural': 'Причины передачи/поступления',
            },
        ),
        migrations.CreateModel(
            name='Reference_values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование переводной единицы')),
                ('unit', models.CharField(max_length=10, verbose_name='Единица измерения')),
                ('multiplier', models.DecimalField(decimal_places=5, max_digits=7, verbose_name='Переводной коэффициент')),
            ],
            options={
                'verbose_name': 'Переводной коэффициент',
                'verbose_name_plural': 'Переводные коэффициенты',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True, verbose_name='Код района')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Наименование района')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
            },
        ),
        migrations.CreateModel(
            name='Waste_collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, verbose_name='Код набора')),
                ('start_date', models.DateField(verbose_name='Дана начала ипользования набора')),
                ('end_date', models.DateField(blank=True, verbose_name='Дана окончания ипользования набора')),
            ],
            options={
                'verbose_name': 'Набор отходов',
                'verbose_name_plural': 'Наборы отходов',
            },
        ),
        migrations.CreateModel(
            name='Waste_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7, verbose_name='Код отхода')),
                ('formation_date', models.DateField(verbose_name='Дата движения отхода')),
                ('quantity_generated', models.DecimalField(blank=True, decimal_places=5, max_digits=8, verbose_name='Объем образования отхода')),
                ('quantity_received', models.DecimalField(blank=True, decimal_places=5, max_digits=8, verbose_name='Объем поступления отхода')),
                ('from_whom', models.CharField(blank=True, max_length=255, verbose_name='От кого поступил отход')),
                ('reas_admis', models.CharField(blank=True, max_length=15, verbose_name='Причина поступления отхода')),
                ('quantity_transf', models.DecimalField(blank=True, decimal_places=5, max_digits=8, verbose_name='Объем переданных отходов')),
                ('for_whom', models.CharField(blank=True, max_length=30, verbose_name='Кому передается отход')),
                ('reas_transf', models.CharField(blank=True, max_length=30, verbose_name='Причина передачи отхода')),
                ('name_officials', models.CharField(max_length=50, verbose_name='ФИО ответственного')),
                ('position_officials', models.CharField(max_length=50, verbose_name='Должность ответственного')),
                ('order_number', models.CharField(max_length=30, verbose_name='Номер приказа о назначении ответственного')),
                ('order_date', models.DateField(verbose_name='Дата приказа о назначении ответственного')),
                ('structural_division', models.CharField(max_length=100, verbose_name='Структурное подразделение')),
                ('region_code', models.CharField(max_length=5, verbose_name='Код района в котором располагается подразделение')),
            ],
            options={
                'verbose_name': 'Данные по отходам',
                'verbose_name_plural': 'Данные по отходам',
            },
        ),
        migrations.CreateModel(
            name='Structural_division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование структурного подразделения')),
                ('lessor', models.CharField(max_length=255, verbose_name='Наименование арендодателя')),
                ('contract_number', models.CharField(max_length=50, verbose_name='Номер договора аренды')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес объекта')),
                ('rental_area', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Площадь аренды')),
                ('open_date', models.DateField(verbose_name='Дата открытия')),
                ('close_date', models.DateField(blank=True, verbose_name='Дата закрытия')),
                ('location_map', models.ImageField(upload_to='', verbose_name='Схема местоположения')),
                ('district_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='ecology.region', to_field='code', verbose_name='Код района')),
                ('waste_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_collection', to='ecology.waste_collection', verbose_name='Набор отходов')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
            },
        ),
        migrations.CreateModel(
            name='Officials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО сотрудника')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('order_number', models.CharField(max_length=30, verbose_name='№ приказа назначения')),
                ('order_date', models.DateField(verbose_name='Дата приказа назначения')),
                ('status', models.BooleanField(verbose_name='Текущий статус')),
                ('corporate_position', models.CharField(choices=[('Руководитель', 'Руководитель'), ('Заместитель', 'Заместитель')], default='Руководитель', max_length=12, verbose_name='Руководитель / Заместитель')),
                ('structural_division', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='str_div_f_Officials', to='ecology.structural_division', verbose_name='Структурное подразделение')),
            ],
            options={
                'verbose_name': 'Уполномоченный сотрудник',
                'verbose_name_plural': 'Уполномоченные сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Waste_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование отхода')),
                ('code', models.CharField(max_length=7, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=7, message='Код д.б. 7-ми значным!'), django.core.validators.MaxLengthValidator(limit_value=7, message='Код д.б. 7-ми значным!')], verbose_name='Код отхода')),
                ('source', models.CharField(max_length=255, verbose_name='Источник образования')),
                ('description', models.CharField(max_length=500, verbose_name='Описание отхода')),
                ('production_rate', models.CharField(max_length=100, verbose_name='Норматив образования')),
                ('status_code', models.CharField(max_length=3, verbose_name='Код физического состояния')),
                ('annual_generation', models.DecimalField(decimal_places=5, max_digits=8, verbose_name='Годовое образвание')),
                ('hint', models.CharField(max_length=255, verbose_name='Подсказка')),
                ('mercury_containing', models.BooleanField(verbose_name='Ртутьсодержащий')),
                ('unit', models.CharField(max_length=10, verbose_name='Единица измерения')),
                ('start_date', models.DateField(verbose_name='Дата начала использования')),
                ('end_date', models.DateField(blank=True, verbose_name='Дата окончания использования')),
                ('picture', models.ImageField(upload_to='', verbose_name='Картинка отхода')),
                ('danger_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='danger_class', to='ecology.danger_class', verbose_name='Класс опасности')),
                ('reason_transf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reason_for_waste', to='ecology.reason_for_transferring', verbose_name='Причина передачи')),
            ],
            options={
                'verbose_name': 'Отход',
                'verbose_name_plural': 'Отходы',
            },
        ),
        migrations.CreateModel(
            name='Waste_receivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование приемщика')),
                ('contract_number', models.CharField(max_length=30, verbose_name='№ договора')),
                ('start_date', models.DateField(verbose_name='Дата заключения договора')),
                ('end_date', models.DateField(blank=True, verbose_name='Дата расторжеения договора')),
                ('reas_transf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecology.reason_for_transferring', verbose_name='Цель приема')),
                ('waste_list', models.ManyToManyField(related_name='waste_codes_receivers', to='ecology.waste_types', verbose_name='Список принимаемых отходов')),
            ],
            options={
                'verbose_name': 'Приемщик',
                'verbose_name_plural': 'Приемщики',
            },
        ),
        migrations.AddField(
            model_name='waste_collection',
            name='waste_codes',
            field=models.ManyToManyField(related_name='waste_codes_collection', to='ecology.waste_types', verbose_name='Список кодов отходов'),
        ),
    ]
