from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from apps.googlemaps.views import RoutesView, RouteView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gmaps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_required(RoutesView.as_view())),
    url(r'^paths/$', login_required(RoutesView.as_view())),
    url(r'path/(?P<id>\d)/$', RoutesView.as_view()),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
)
