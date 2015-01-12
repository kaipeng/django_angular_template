
from django.conf.urls import patterns, url
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


urlpatterns = patterns("frontend.views",
                       url(r'^$', RedirectView.as_view(url='site/', permanent=True)),
                       ("^site/$", TemplateView.as_view(template_name="frontend.html"))
                       #("^$", TemplateView.as_view(template_name="frontend.html"))
                       )
urlpatterns += patterns('django.contrib.staticfiles.views',
                        url(r'^(?P<path>.*)$', 'serve'),
                        )
