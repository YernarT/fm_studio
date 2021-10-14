from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='img/user/avatar/',
                               default='img/user/avatar/default-avatar.png', verbose_name='Аватар пользователя')

    class Meta:
        db_table = 'user'
        verbose_name = 'пользователь'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.username}'
