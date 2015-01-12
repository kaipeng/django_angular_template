
from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns("frontend.views",
                       )
urlpatterns += patterns('django.contrib.staticfiles.views',
                        url(r'^(?P<path>.*)$', 'serve'),
                        )
