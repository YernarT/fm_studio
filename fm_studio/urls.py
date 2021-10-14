from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^user/', include('user.urls', namespace='user')),
    url(r'^', include('music.urls', namespace='music')),

    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
