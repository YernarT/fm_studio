# Generated by Django 3.2.8 on 2022-02-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220220_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='user_2022022100', max_length=24, verbose_name='атау'),
        ),
    ]