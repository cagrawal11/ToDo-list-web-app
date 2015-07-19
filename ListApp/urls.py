from django.conf.urls import patterns, include, url
from django.contrib import admin

from ListApp import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ToDo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index_view, name='index'),
	url(r'^addTask.html$', views.add_task, name='add_task'),
	url(r'^show_all.html$', views.show_all, name='show_all'),
	url(r'^index.html$', views.sign_up, name='sign_up'),
	url(r'^abc.html$', views.sign_in, name='sign_in')
)
