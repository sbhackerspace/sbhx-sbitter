from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('sbitter_app.views',
    url(r'^$', 'view_my_sbits', name='index'),
    url(r'^search/$', 'search', name='search'),
    url(r'^login/$', login, kwargs=dict(template_name='login.html'),
        name='login'),
    url(r'^logout/$', logout, kwargs=dict(next_page='/'),
        name='logout'),
)
