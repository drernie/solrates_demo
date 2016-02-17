from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from models import Assumptions


def index(request):
    scenarios = Assumptions.objects.all()
    context = {
        'scenarios': scenarios,
    }
    return render(request, 'scenarios/index.html', context)

def detail(request, assumptions_id):
    a = Assumptions.objects.get(pk=assumptions_id)
    return HttpResponse("You're looking at scenario %s." % a)

def results(request, assumptions_id):
    a = Assumptions.objects.get(pk=assumptions_id)
    response = "You're looking at the results of scenario %s."
    return HttpResponse(response % a)
