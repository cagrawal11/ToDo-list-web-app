from django.conf.urls import patterns, include, url
from django.contrib import admin

from ListApp import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ToDo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index_view, name='index'),
	url(r'^$', views.add_task, name='addTask')
)
