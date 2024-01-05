from django.contrib import admin
from django.db.models import QuerySet

from .models import *


@admin.register(Waste_types)
class Waste_typesAdmin(admin.ModelAdmin):
    """Виды отходов"""
    list_display = ['name', 'code', 'start_date', 'end_date']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['code', 'name'] #поля по которым будет происходит сортировка (preview)
    list_per_page = 13 #пагинация (preview)
    search_fields = ['code', 'name'] #поле поиска (preview)


@admin.register(Reason_for_transferring)
class Reason_for_transferringAdmin(admin.ModelAdmin):
    """Причины передачи/получения отходов"""
    list_display = ['code', 'name']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['name']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)


@admin.register(Danger_class)
class Danger_classAdmin(admin.ModelAdmin):
    """Класс опасности отходов"""
    list_display = ['code', 'name']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['code']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)


@admin.register(Structural_division)
class Structural_divisionAdmin(admin.ModelAdmin):
    """Структурное подразделение"""
    list_display = ['name', 'lessor', 'district_code', 'open_date',
                    'close_date']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['name']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)
    search_fields = ['name']  # поле поиска (preview)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    """Районы расположения"""
    list_display = ['code', 'name']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['code']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)


@admin.register(Waste_collection)
class Waste_collectionAdmin(admin.ModelAdmin):
    """Наборы отходов"""
    list_display = ['code', 'start_date',
                    'end_date']  # дополнить списком?? #список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['code']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)
    filter_horizontal = ['waste_codes'] #горизонтальный виджет


@admin.register(Officials)
class OfficialsAdmin(admin.ModelAdmin):
    """Должностные лица"""
    list_display = ['name', 'position', 'status', 'corporate_position']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['status', 'structural_division', 'corporate_position']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)
    search_fields = ['name']  # поле поиска (preview)


@admin.register(Waste_receivers)
class Waste_receiversAdmin(admin.ModelAdmin):
    """Приемщики отходов"""
    list_display = ['name', 'start_date',
                    'end_date']  # Дополнить списком?? #список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['name']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)
    search_fields = ['name']  # поле поиска (preview)
    filter_horizontal = ['waste_list'] #горизонтальный виджет


@admin.register(Landfill_facility)
class Landfill_facilityAdmin(admin.ModelAdmin):
    """Объекты захоронения"""
    list_display = ['code', 'name']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['name']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)


@admin.register(Reference_values)
class Reference_valuesAdmin(admin.ModelAdmin):
    """Переводные коэффициенты (константы)"""
    list_display = ['name', 'unit', 'multiplier']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['name']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)


@admin.register(Company_data)
class Company_dataAdmin(admin.ModelAdmin):
    """Данные юридического лица"""
    list_display = ['start_date', 'num_subdiv', 'e_mail']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['start_date']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    """Автомобили"""
    list_display = ['name', 'start_date', 'end_date']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['-start_date']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)


@admin.register(Passport_data)
class Passport_dataAdmin(admin.ModelAdmin):
    """Данные для Экологического паспорта"""
    list_display = ['year', 'name', 'unit', 'quantity']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['year', 'name']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 11  # пагинация (preview)


@admin.register(Licence)
class ModelNameAdmin(admin.ModelAdmin):
    """Перечень разрешений, лицензий"""
    list_display = ['number', 'start_date', 'end_date']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['start_date']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 13  # пагинация (preview)


@admin.register(Waste_data)
class Waste_dataAdmin(admin.ModelAdmin):
    """Движение отходов"""
    list_display = ['code', 'formation_date', 'quantity_generated', 'quantity_received', 'from_whom', 'quantity_transf',
                    'structural_division', 'region_code']  # список отображаемых в админке полей (preview)
    list_editable = []  # список редактируемых полей (preview)
    ordering = ['formation_date', 'structural_division']  # поля по которым будет происходит сортировка (preview)
    list_per_page = 100  # пагинация (preview)
    search_fields = ['code', 'structural_division']  # поле поиска (preview)
