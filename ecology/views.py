from django.shortcuts import render, get_object_or_404

from .models import *
from .work import *


def test(request):
    waste = Waste_types.actual.all()
    waste_stok = Waste_types.objects.filter(code='1471501')
    # data = get_stok('Е.А.Богомья')
    context = {
        'title': 'Экология',
        'waste': waste,
        'wa': waste_stok,
        'data': data,
    }
    return render(request, 'ecology/ecology.html', context=context)
