from django.db import models


class Waste_types(models.Model):
    """Виды отходов"""
    name = models.CharField(max_length=255, unique=True, verbose_name='Наименование отхода')
    code = models.CharField(max_length=7, verbose_name='Код отхода')
    danger_class = models.ForeignKey('Danger_class', to_field='name', on_delete=models.PROTECT,
                                     related_name='danger_class',
                                     verbose_name='Класс опасности')
    source = models.CharField(max_length=255, verbose_name='Источник образования')
    description = models.CharField(max_length=500, verbose_name='Описание отхода')
    production_rate = models.CharField(max_length=100, verbose_name='Норматив образования')
    status_code = models.CharField(max_length=3, verbose_name='Код физического состояния')
    reason_transf = models.ForeignKey('Reason_for_transferring', to_field='name', on_delete=models.PROTECT, related_name='reason',
                                      verbose_name='Причина передачи')
    annual_generation = models.DecimalField(max_digits=8, decimal_places=5, verbose_name='Годовое образвание')
    hint = models.CharField(max_length=255, verbose_name='Подсказка')
    mercury_containing = models.BooleanField(verbose_name='Ртутьсодержащий')
    unit = models.CharField(max_length=10, verbose_name='Единица измерения')
    start_date = models.DateField(verbose_name='Дата начала использования')
    end_date = models.DateField(blank=True, verbose_name='Дата окончания использования')
    picture = models.ImageField(verbose_name='Картинка отхода')

    class Meta:
        verbose_name = 'Отход'
        verbose_name_plural = 'Отходы'

    def __str__(self):
        return f'{self.name} | {self.code}'


class Reason_for_transferring(models.Model):
    """Причины передачи/получения отходов"""
    name = models.CharField(max_length=30, verbose_name='Наименование причины')
    code = models.CharField(max_length=2, unique=True, verbose_name='Код причины')
    short_name = models.CharField(max_length=10, verbose_name='Краткое наименование причины')

    class Meta:
        verbose_name = 'Причина'
        verbose_name_plural = 'Причины передачи/поступления'

    def __str__(self):
        return self.name


class Danger_class(models.Model):
    """Класс опасности отходов"""
    code = models.CharField(max_length=2, verbose_name='Код класса опасности')
    name = models.CharField(max_length=30, unique=True, verbose_name='Нименование класса')
    short_name = models.CharField(max_length=10, verbose_name='Краткое наименование класса')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы опаснсоти'

    def __str__(self):
        return self.name


class Structural_division(models.Model):
    """Структурное подразделение"""
    name = models.CharField(max_length=100, verbose_name='Наименование структурного подразделения')
    lessor = models.CharField(max_length=255, verbose_name='Наименование арендодателя')
    contract_number = models.CharField(max_length=50, verbose_name='Номер договора аренды')
    district_code = models.ForeignKey('Region', to_field='code', on_delete=models.PROTECT, related_name='region',
                                      verbose_name='Код района')
    address = models.CharField(max_length=255, verbose_name='Адрес объекта')
    rental_area = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Площадь аренды')
    open_date = models.DateField(verbose_name='Дата открытия')
    close_date = models.DateField(blank=True, verbose_name='Дата закрытия')
    waste_collection = models.CharField(max_length=5, verbose_name='Набор отходов')
    location_map = models.ImageField(verbose_name='Схема местоположения')

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name


class Region(models.Model):
    """Районы расположения"""
    code = models.CharField(max_length=5, verbose_name='Код района')
    name = models.CharField(max_length=50, unique=True, verbose_name='Наименование района')

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return f'{self.name} | {self.code}'


class Waste_collection(models.Model):
    """Наборы отходов"""
    code = models.CharField(max_length=5, verbose_name='Код набора')
    start_date = models.DateField(verbose_name='Дана начала ипользования набора')
    end_date = models.DateField(blank=True, verbose_name='Дана окончания ипользования набора')
    waste_codes = models.ForeignKey(verbose_name='Коды отходов')  # надо проработать и понять как правильно

    class Meta:
        verbose_name = 'Набор отходов'
        verbose_name_plural = 'Наборы отходов'

    def __str__(self):
        return self.code


class Officials(models.Model):
    """Должностные лица"""
    name = models.CharField(max_length=50, verbose_name='ФИО сотрудника')
    position = models.CharField(max_length=50, verbose_name='Должность')
    order_number = models.CharField(max_length=30, verbose_name='№ приказа назначения')
    order_date = models.DateField(verbose_name='Дата приказа назначения')
    structural_division = models.ForeignKey('Structural_division', to_field='name', on_delete=models.PROTECT,
                                            verbose_name='Структурное подразделение')
    status = models.BooleanField(verbose_name='Текущий статус')
    corporate_position = models.CharField(max_length=10,
                                          choices=[('Руководитель', 'Руководитель'), ('Заместитель', 'Заместитель')],
                                          verbose_name='Руководитель / Заместитель')

    class Meta:
        verbose_name = 'Уполномоченный сотрудник'
        verbose_name_plural = 'Уполномоченные сотрудники'

    def __str__(self):
        return f'{self.name} | {self.position} | {self.status}'


class Waste_receivers(models.Model):
    """Приемщики отходов"""
    name = models.CharField(max_length=255, verbose_name='Наименование приемщика')
    contract_number = models.CharField(max_length=30, verbose_name='№ договора')
    start_date = models.DateField(verbose_name='Дата заключения договора')
    end_date = models.DateField(blank=True, verbose_name='Дата расторжеения договора')
    reas_transf = models.ForeignKey('Reason_for_transferring', to_field='name', on_delete=models.PROTECT, verbose_name='Цель приема')
    waste_list = models.CharField(verbose_name='Список принимаемых отходов')  # как сохранять спсиок?

    class Meta:
        verbose_name = 'Приемщик'
        verbose_name_plural = 'Приемщики'

    def __str__(self):
        return self.name


class Landfill_facility(models.Model):
    """Объекты захоронения"""
    code = models.CharField(max_length=2, verbose_name='Код объекта захоронения')
    name = models.CharField(max_length=50, unique=True, verbose_name='Наименование объекта захоронения')

    class Meta:
        verbose_name = 'Объект захоронения'
        verbose_name_plural = 'Объекты захоронения'

    def __str__(self):
        return self.name


class Reference_values(models.Model):
    """Переводные коэффициенты (константы)"""
    name = models.CharField(max_length=50, verbose_name='Наименование переводной единицы')
    unit = models.CharField(max_length=10, verbose_name='Единица измерения')
    multiplier = models.DecimalField(max_digits=7, decimal_places=5, verbose_name='Переводной коэффициент')

    class Meta:
        verbose_name = 'Переводной коэффициент'
        verbose_name_plural = 'Переводные коэффициенты'

    def __str__(self):
        return self.name


class Company_data(models.Model):
    """Данные юридического лица"""
    start_date = models.DateField(verbose_name='Дата начала использования данных')
    company_name = models.CharField(max_length=100, verbose_name='Наименование юридического лица')
    OKED = models.CharField(max_length=100, verbose_name='Вид деятельности по ОКЭД')
    UNP = models.CharField(max_length=9, verbose_name='УНП')
    UNP_date = models.DateField(verbose_name='Дата УНП')
    OKPO = models.CharField(max_length=11, verbose_name='ОКПО')
    num_subdiv = models.IntegerField(verbose_name='Количество структурных подразделений')
    postal_address = models.CharField(max_length=255, verbose_name='Почтовый адресс')
    legal_address = models.CharField(max_length=255, verbose_name='Юридический адресс')
    e_mail = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Данные компании'
        verbose_name_plural = 'Данные компании'

    def __str__(self):
        return self.company_name


class Cars(models.Model):
    """Автомобили """
    name = models.CharField(max_length=50, verbose_name='Марка автомобиля')
    car_type = models.CharField(max_length=15, verbose_name='Тип автомоиля')
    prod_year = models.DateField(verbose_name='Дата производства')
    eco_class = models.CharField(max_length=5, verbose_name='Экологический класс')
    start_date = models.DateField(verbose_name='Дата начала эксплуатации')
    end_date = models.DateField(blank=True, verbose_name='Дата окончания эксплуатации')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.name


class Passport_data(models.Model):
    """Данные для Экологического паспорта"""
    year = models.DateField(verbose_name='Год данных')
    name = models.CharField(max_length=100, verbose_name='Наименование показателя')
    unit = models.CharField(max_length=10, verbose_name='Единица измерения')
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Значение показателя')

    class Meta:
        verbose_name = 'Данные для паспорта'
        verbose_name_plural = 'Данные для паспорта'

    def __str__(self):
        return self.name


class licence(models.Model):
    """Перечень разрешений, лицензий"""
    number = models.CharField(max_length=10, verbose_name='Регистрационный номер документа')
    start_date = models.DateField(verbose_name='Дата начала действия')
    end_date = models.DateField(verbose_name='Дата окончания действия')
    conditions = models.CharField(max_length=255, verbose_name='Условия разрешения/лицензии')
    permit_waste = models.DecimalField(max_digits=7, decimal_places=5,
                                       verbose_name='Количество отходов согласно разрешения (всего)')
    waste_III = models.DecimalField(max_digits=7, decimal_places=5,
                                    verbose_name='Количество отходов III класса, согласно разрешения (всего)')

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'

    def __str__(self):
        return self.number


class Waste_data(models.Model):
    """Движение отходов"""
    code = models.CharField(max_length=7, verbose_name='Код отхода')
    formation_date = models.DateField(verbose_name='Дата движения отхода')
    quantity_generated = models.DecimalField(max_digits=8, decimal_places=5, verbose_name='Объем образования отхода')
    quantity_received = models.DecimalField(max_digits=8, decimal_places=5, verbose_name='Объем поступления отхода')
    from_whom = models.CharField(max_length=50, verbose_name='От кого поступил отход')
    reas_admis = models.CharField(max_length=50, verbose_name='Причина поступления отхода')
    quantity_transf = models.DecimalField(max_digits=8, decimal_places=5, verbose_name='Объем переданных отходов')
    for_whom = models.CharField(max_length=50, verbose_name='Кому передается отход')
    reas_transf = models.CharField(max_length=50, verbose_name='Причина передачи отхода')
    name_officials = models.CharField(max_length=30, verbose_name='ФИО ответственного')
    position_officials = models.CharField(max_length=30, verbose_name='Должность ответственного')
    order_number = models.CharField(max_length=10, verbose_name='Номер приказа о назначении ответственного')
    order_date = models.DateField(verbose_name='Дата приказа о назначении ответственного')
    structural_division = models.CharField(max_length=30, verbose_name='Структурное подразделение')
    region_code = models.CharField(max_length=5, verbose_name='Код района в котором располагается подразделение')

    class Meta:
        verbose_name = 'Данные по отходам'
        verbose_name_plural = 'Данные по отходам'

    def __str__(self):
        return f'{self.code} | {self.structural_division}'
