from django.shortcuts import render
from django.http import HttpResponse
from models import Assumptions


def index(request):
    return HttpResponse("Welcome to the SolRates Scenarios Demo.")

def detail(request, assumptions_id):
    a = Assumptions.objects.get(pk=assumptions_id)
    return HttpResponse("You're looking at scenario %s." % a)

def results(request, assumptions_id):
    a = Assumptions.objects.get(pk=assumptions_id)
    response = "You're looking at the results of scenario %s."
    return HttpResponse(response % a)
