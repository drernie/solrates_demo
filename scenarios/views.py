from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Assumptions
from django.views import generic

class ScenariosList(generic.ListView):
    model = Assumptions

class ScenariosDetail(generic.DetailView):
    model = Assumptions

class ScenarioCreate(generic.CreateView):
    model = Assumptions
    fields = [
        'installers_start',
        'installers_weekly_growth',
        'deal_frequency_in_weeks',
        'deal_latency_in_weeks',
        'deal_revenue_thousands',
        'target_monthly_revenue',
    ]

