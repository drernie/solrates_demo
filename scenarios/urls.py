from django.conf.urls import url

from . import views
app_name = 'scenarios'
urlpatterns = [
    url(r'^$', views.ScenariosList.as_view(), name='index'),
    url(r'^(?P<assumptions_id>[0-9]+)/$', views.detail, name='detail'),
]
