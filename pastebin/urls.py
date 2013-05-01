from django.conf.urls import *
from django.conf import settings
from django.conf.urls import patterns
from django.views.generic import TemplateView

from .views import FormIndex
from .views import PasteDetails
from .views import Plain

urlpatterns = patterns('pastebin.views',
        url(r'^$', FormIndex.as_view(), name='djpaste_index'),
        url(r'^help/$', TemplateView.as_view(template_name='djpaste/help.html'), name='djpaste_help'),
        url(r'^paste/(?P<id>\d+)/$', 'paste_details', name='djpaste_paste_details'),
        url(r'^plain/(?P<id>\d+)/$', 'plain', name='djpaste_plain'),
        url(r'^html/(?P<id>\d+)/$', 'html', name='djpaste_html'),


)

if settings.DEBUG:    
    media_dir = settings.MEDIA_ROOT
    urlpatterns += patterns('',
            url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media_dir}),
        )

