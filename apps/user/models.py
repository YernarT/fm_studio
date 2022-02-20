from django.db import models
from datetime import datetime


class User(models.Model):
    username = models.CharField(max_length=24, default='user_' + datetime.strftime(
        datetime.now(), '%Y%m%d%H'), verbose_name='атау')
    phone = models.CharField(max_length=11, unique=True,
                             verbose_name='телефон нөмер')
    password = models.CharField(max_length=255, verbose_name='құпия сөз')
    is_admin = models.BooleanField(
        default=False, blank=False, verbose_name='админ')

    birthday = models.DateField(
        null=True, blank=True, verbose_name='туған күн')
    gender = models.BooleanField(
        choices=((True, 'Ер'), (False, 'Әйел')), default=False, blank=False, verbose_name='жыныс')
    avatar = models.ImageField(upload_to='img/user/avatar/',
                               default='img/user/avatar/default-avatar.png', blank=False, verbose_name='аватар')
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='құрылған уақыт')

    class Meta:
        db_table = 'user'
        verbose_name = 'пайдаланушы'
        verbose_name_plural = 'пайдаланушылар'

    def __str__(self):
        return f'{self.phone}'
