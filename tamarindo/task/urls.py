from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('tamarindo.task.views',
    (r'^$', 'index'),
)