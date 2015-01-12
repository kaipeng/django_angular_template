from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView


from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('dashboard.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin$', RedirectView.as_view(url='/admin/')),
    url(r'^home$', RedirectView.as_view(url='/home/')),
    url(r'^api$', RedirectView.as_view(url='/api/')),
    url(r'^api-auth$', RedirectView.as_view(url='/api-auth/')),

    url(r'', include('frontend.urls')),

]
