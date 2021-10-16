from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from django.views.static import serve
from fm_studio import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^user/', include('user.urls', namespace='user')),
    url(r'^', include('music.urls', namespace='music')),

    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]
