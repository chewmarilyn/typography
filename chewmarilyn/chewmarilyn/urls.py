from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'chewmarilyn.views.home', name='home'),
    # url(r'favicon.ico/', 'chewmarilyn.views.favicon', name='favicon'),
    url(r'^upload/$', 'chewmarilyn.views.upload', name='upload'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# only for development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
