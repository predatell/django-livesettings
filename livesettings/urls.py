from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.site_settings, {}, 'satchmo_site_settings'),
    re_path(r'^export/$', views.export_as_python, {}, 'settings_export'),
    re_path(r'^(?P<group>[^/]+)/$', views.group_settings),
]