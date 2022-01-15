from django.contrib import admin
from .models import *

admin.site.register(Music)
admin.site.register(MusicType)
admin.site.register(MusicLike)
admin.site.register(MusicComment)
