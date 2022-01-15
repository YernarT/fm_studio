from django.db import models


class MusicType(models.Model):
    name = models.CharField(max_length=40, verbose_name='жанр атауы')

    class Meta:
        db_table = 'music_type'
        verbose_name = 'музыка жанр'
        verbose_name_plural = 'музыка жанрлары'

    def __str__(self):
        return f'{self.name}'


class Music(models.Model):
    name = models.CharField(max_length=40, verbose_name='музыка атауы')
    music = models.FileField(upload_to='audio/', verbose_name='музыка файлы')
    music_type = models.ManyToManyField(
        to='MusicType', related_name='music_types', verbose_name='мазыка жанры')
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


class MusicComment(models.Model):
    content = models.CharField(max_length=255, verbose_name='пікір')
    music = models.ForeignKey(
        to='Music', on_delete=models.CASCADE, verbose_name='музыка')
    user = models.ForeignKey(
        to='user.User', on_delete=models.CASCADE, verbose_name='пайдаланушы')

    class Meta:
        db_table = 'music_comment'
        verbose_name = 'пікір'
        verbose_name_plural = 'пікірлер'

    def __str__(self):
        return f'{self.content}'
