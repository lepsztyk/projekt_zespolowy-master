from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout),
]
