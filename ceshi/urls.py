from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'ceshi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^geo/', include('geo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
)
