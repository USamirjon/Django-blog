from django.db import models


class Users(models.Model):
    login = models.CharField('Логин', max_length=200)
    password = models.CharField('Пароль', max_length=200)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

