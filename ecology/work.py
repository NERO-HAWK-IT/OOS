from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When

from ecology.models import *

class Waste_stok:
    def __init__(self, code: str):
        self.code = code






def stok(code: str) -> float:
    result = Waste_data.objects.filter(code=code).aggregate(
        res=(Sum('quantity_generated') + Sum('quantity_received') - Sum('quantity_transf')))
    return result['res']
