from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

urlpatterns = patterns('pastebin.views',
        url(r'^$', 'index', name='djpaste_index'),
        url(r'^help/$', direct_to_template, {'template':'djpaste/help.html'}, name='djpaste_help'),
        url(r'^paste/(?P<id>\d+)/$', 'paste_details', name='djpaste_paste_details'),
        url(r'^plain/(?P<id>\d+)/$', 'plain', name='djpaste_plain'),
        url(r'^html/(?P<id>\d+)/$', 'html', name='djpaste_html'),
)

if settings.DEBUG:    
    media_dir = settings.MEDIA_ROOT
    urlpatterns += patterns('',
            url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media_dir}),
        )

