from django.db.models import Sum, FloatField
from django.db.models.functions import Coalesce

from ecology.models import *


class Waste_stok:
    def __init__(self, code: str):
        self.code = code


def get_stok(name: str):
    division = Officials.actual.get(name=name).structural_division
    division_id = division.pk  # Получаем id подразделения
    division_name = division.name  # Получаем наименование подразделения
    collection = [el.code for el in Waste_collection.actual.get(
        division=division_id).waste_codes.all()]  # Получаем актуальный список отходов для подразделения
    for code in collection:  # По каждому отходу из списка
        data = Waste_data.objects.filter(code=code, structural_division=division_name)
        generated = data.aggregate(res=(Coalesce(Sum('quantity_generated', output_field=FloatField()), 0.0)))[
            'res']  # получаем суммарное образовавание отхода в подразделении
        received = data.aggregate(res=(Coalesce(Sum('quantity_received', output_field=FloatField()), 0.0)))[
            'res']  # получаем суммарное поступленеи отхода в подразделении
        transf = data.aggregate(res=(Coalesce(Sum('quantity_transf', output_field=FloatField()), 0.0)))[
            'res']  # получаем суммарное перемещение отхода из подразделения
        stock = round((generated + received - transf), 5)  # получаем остаток отхода на хранении в подразделении
        print(f'{code} - {stock}')
