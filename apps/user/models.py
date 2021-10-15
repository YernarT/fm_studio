from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthday = models.DateField(
        null=True, blank=True, verbose_name='туған күн',)
    gender = models.BooleanField(
        choices=((True, 'Ер'), (False, 'Әйел')), verbose_name='Жыныс')
    avatar = models.ImageField(upload_to='img/user/avatar/',
                               default='img/user/avatar/default-avatar.png', verbose_name='аватар')

    class Meta:
        db_table = 'user'
        verbose_name = 'пайдаланушы'
        verbose_name_plural = 'пайдаланушылар'

    def __str__(self):
        return f'{self.username}'
