from django.conf.urls import patterns, include, url
from django.contrib import admin
from server.urls import router_v1
import rest_framework

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api_v1/', include(router_v1.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)
