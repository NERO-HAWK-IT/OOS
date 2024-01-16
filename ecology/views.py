from django.shortcuts import render, get_object_or_404

from .models import *

def test(request, pk):
    waste = get_object_or_404(Waste_types, pk=pk)
    context = {
        'title': 'Экология',
        'waste': waste,
    }
    return render(request, 'ecology/ecology.html', context=context)

