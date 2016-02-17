from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Assumptions


def index(request):
    scenarios = Assumptions.objects.all()
    context = {
        'scenarios': scenarios,
    }
    return render(request, 'scenarios/index.html', context)

def detail(request, assumptions_id):
    context = {
        'scenario': get_object_or_404(Assumptions, pk=assumptions_id),
    }
    return render(request, 'scenarios/detail.html', context)

def results(request, assumptions_id):
    a = Assumptions.objects.get(pk=assumptions_id)
    response = "You're looking at the results of scenario %s."
    return HttpResponse(response % a)
