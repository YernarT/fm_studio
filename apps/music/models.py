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
    music_type = models.ManyToManyField(to='MusicType', related_name='music_types', verbose_name='мазыка жанры')


    class Meta:
        db_table = 'music'
        verbose_name = 'музыка'
        verbose_name_plural = 'музыкалар'

    def __str__(self):
        return f'{self.name}'


