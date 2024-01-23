from django.shortcuts import render, get_object_or_404

from .models import *

def test(request):
    waste = Waste_types.actual.all()

    context = {
        'title': 'Экология',
        'waste': waste,
    }
    return render(request, 'ecology/ecology.html', context=context)

