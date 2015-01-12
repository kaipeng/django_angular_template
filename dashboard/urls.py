
from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns("dashboard.views",
                       )
urlpatterns += patterns('django.contrib.staticfiles.views',
                        url(r'^(?P<path>.*)$', 'serve'),
                        )
