from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=24, verbose_name='альбом атауы')
    cover = models.ImageField(upload_to='img/music/album-cover/',
                              null=True, blank=True, verbose_name='альбом суреті')
    author = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, null=True, verbose_name='пайдаланушы')

    class Meta:
        db_table = 'music_album'
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомдар'

    def __str__(self):
        return f'{self.name}'


class AlbumMusic(models.Model):
    album = models.ForeignKey(
        'Album', on_delete=models.CASCADE, verbose_name='альбум')
    music = models.ForeignKey(
        to='Music', on_delete=models.CASCADE, verbose_name='музыка')

    class Meta:
        db_table = 'album_music'
        verbose_name = 'альбумдағы музыка'
        verbose_name_plural = 'альбумдағы музыкалар'

    def __str__(self):
        return f'{self.music.name}'


class AlbumComment(models.Model):
    content = models.CharField(max_length=255, verbose_name='пікір')
    album = models.ForeignKey(
        to='Album', on_delete=models.CASCADE, verbose_name='альбом')
    user = models.ForeignKey(
        to='user.User', on_delete=models.CASCADE, verbose_name='пайдаланушы')

    class Meta:
        db_table = 'album_comment'
        verbose_name = 'пікір'
        verbose_name_plural = 'пікірлер'

    def __str__(self):
        return f'{self.content}'


class MusicType(models.Model):
    name = models.CharField(max_length=24, unique=True, verbose_name='жанр атауы')

    class Meta:
        db_table = 'music_type'
        verbose_name = 'музыка жанр'
        verbose_name_plural = 'музыка жанрлары'

    def __str__(self):
        return f'{self.name}'


class Music(models.Model):
    name = models.CharField(max_length=24, verbose_name='музыка атауы')
    music = models.FileField(upload_to='audio/', verbose_name='музыка файлы')
    music_type = models.ManyToManyField(
        to='MusicType', related_name='music_types', verbose_name='музыка жанры')
    author = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, null=True, verbose_name='авторы')
    views = models.IntegerField(default=0, verbose_name='есту саны')
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='құрылған уақыт')

    class Meta:
        db_table = 'music'
        verbose_name = 'музыка'
        verbose_name_plural = 'музыкалар'

    def __str__(self):
        return f'{self.name}'


class MusicLike(models.Model):
    music = models.ForeignKey(
        to='Music', on_delete=models.CASCADE, verbose_name='музыка')
    user = models.ForeignKey(
        to='user.User', on_delete=models.CASCADE, verbose_name='пайдаланушы')

    class Meta:
        db_table = 'music_like'
        verbose_name = 'лайк'
        verbose_name_plural = 'лайктар'

    def __str__(self):
        return f'{self.user}'


class Favorites(models.Model):
    name = models.CharField(max_length=24, verbose_name='таңдаулар атауы')
    creator = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='құрушы')
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='құрылған уақыт')

    class Meta:
        db_table = 'music_favorites'
        verbose_name = 'таңдаулар'
        verbose_name_plural = 'таңдаулар'

    def __str__(self):
        return f'{self.name}'


class FavoriteMusic(models.Model):
    favorites = models.ForeignKey(
        'Favorites', on_delete=models.CASCADE, verbose_name='таңдаулар')
    music = models.ForeignKey(
        to='Music', on_delete=models.CASCADE, verbose_name='музыка')

    class Meta:
        db_table = 'favorites_music'
        verbose_name = 'таңдаулардағы музыка'
        verbose_name_plural = 'таңдаулардағы музыкалар'

    def __str__(self):
        return f'{self.music.name}'
