from django.shortcuts import render
from django.http import HttpResponse
from models import Assumptions


def index(request):
    scenarios = Assumptions.objects.all()
    output = ', '.join(["%s" % q for q in scenarios])
    return HttpResponse(output)

def detail(request, assumptions_id):
    a = Assumptions.objects.get(pk=assumptions_id)
    return HttpResponse("You're looking at scenario %s." % a)

def results(request, assumptions_id):
    a = Assumptions.objects.get(pk=assumptions_id)
    response = "You're looking at the results of scenario %s."
    return HttpResponse(response % a)
