from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^simpleq/$', 'simpleq.views.index'),
    #url(r'^simpleq/(?P<question_id>\d+)/$', 'simpleq.views.question_detail'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^questions/$', 'simpleq.views.index', name="questions"),
    url(r'^questions/(?P<question_id>\d+)/$', 'simpleq.views.question_detail', name='question_detail'),
)
