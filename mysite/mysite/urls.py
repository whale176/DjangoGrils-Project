from django.conf.urls import patterns, include, url
from django.contrib import admin
from trips.views import hello_world, home, post_detail, show_form

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello_world),
    url(r'^$', home),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^showform/', show_form),
    url(r'^accounts/', include('allauth.urls')),
)
