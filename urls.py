from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^system/', include('skylime_admin.limeade.system.urls')),
    (r'^mail/',   include('skylime_admin.limeade.mail.urls')),
    (r'^admin/',  include(admin.site.urls)),
    (r'^accounts/login/$',  'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    (r'^accounts/change_password/$', 'django.contrib.auth.views.password_change'),
    (r'^accounts/change_password/done/$', 'django.contrib.auth.views.password_change_done'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)