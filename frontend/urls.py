
from django.conf.urls import patterns, url
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = patterns("frontend.views",
                       ("^$", TemplateView.as_view(template_name="site/index.html"))
                       )
urlpatterns += patterns('django.contrib.staticfiles.views',
                        url(r'^site/(?P<path>.*)$', 'serve'),
                        )
