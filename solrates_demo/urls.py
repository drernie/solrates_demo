from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'solrates_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index' ),
    url(r'^scenarios/', include('scenarios.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
