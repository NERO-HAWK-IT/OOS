from django.shortcuts import render, get_object_or_404

from .models import *
from .work import stok

def test(request):
    waste = Waste_types.actual.all()
    waste_stok = stok('')
    context = {
        'title': 'Экология',
        'waste': waste,
        'wa': waste_stok,
    }
    return render(request, 'ecology/ecology.html', context=context)
