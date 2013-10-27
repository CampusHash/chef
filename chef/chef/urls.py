from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Tastypie stuff
from tastypie.api import Api
from api.resources import ProfileResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(ProfileResource())
v1_api.register(UserResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chef.views.home', name='home'),
    # url(r'^chef/', include('chef.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # API URL Conf
    (r'^api/', include(v1_api.urls)),
)
