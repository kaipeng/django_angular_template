
from django.conf.urls import patterns, url
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = patterns("dashboard.views",
                       (r'^$', TemplateView.as_view(template_name="dashboard.html"))
                       )
urlpatterns += patterns('django.contrib.staticfiles.views',
                        url(r'^(?P<path>.*)$', 'serve'),
                        )
