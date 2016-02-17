from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Assumptions
from django.views import generic

class ScenariosList(generic.ListView):
    model = Assumptions

class ScenariosDetail(generic.DetailView):
    model = Assumptions
