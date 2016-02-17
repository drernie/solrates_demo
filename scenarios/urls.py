from django.conf.urls import url

from . import views
app_name = 'scenarios'
urlpatterns = [
    url(r'^$', views.ScenariosList.as_view(), name='index'),
    url(r'author/add/$', views.ScenarioCreate.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/$', views.ScenariosDetail.as_view(), name='detail'),
]
