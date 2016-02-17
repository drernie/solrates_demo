from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Greetings</h1>Welcome to Dr. Ernie's SolRates demo app.<p> Check <a href='/scenarios/'>here</a> to explore growth scenarios.")
