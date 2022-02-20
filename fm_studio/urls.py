from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from django.views.static import serve
from fm_studio import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^api/user/', include('user.urls')),
    url(r'^api/music/', include('music.urls')),

    url(r'^media/(?P<path>.*)$', serve,
        {"document_root": settings.MEDIA_ROOT}),
]
