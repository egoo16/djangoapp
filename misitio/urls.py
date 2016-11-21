from django.conf.urls import include, url
from django.contrib.auth import views
import django.contrib.auth.views
from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'misitio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('citas.urls')),
    #url(r'', include('cine.urls')),
]
