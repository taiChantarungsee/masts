from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^masts/', include('mast_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
