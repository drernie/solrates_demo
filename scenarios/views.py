from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Assumptions
from django.views import generic

class ScenariosList(generic.ListView):
    model = Assumptions

def detail(request, assumptions_id):
    context = {
        'scenario': get_object_or_404(Assumptions, pk=assumptions_id),
    }
    return render(request, 'scenarios/detail.html', context)

