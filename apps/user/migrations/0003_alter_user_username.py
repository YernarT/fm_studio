# Generated by Django 3.2.8 on 2022-01-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220115_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='user_2022011702', max_length=24, verbose_name='атау'),
        ),
    ]
