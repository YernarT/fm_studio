from django.contrib import admin
from .models import *

admin.site.register(Music)
admin.site.register(MusicType)
admin.site.register(MusicLike)

admin.site.register(Album)
admin.site.register(AlbumComment)

admin.site.register(Favorites)
admin.site.register(FavoriteMusic)
