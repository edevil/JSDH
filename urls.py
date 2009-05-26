from django.conf.urls.defaults import *
import os

urlpatterns = patterns('',
    (r'^$', 'jsdh.views.index'),
    (r'^finish_dh/$', 'jsdh.views.finish_dh'),    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.abspath(os.path.join(os.path.dirname(__file__), 'media'))}),
)
