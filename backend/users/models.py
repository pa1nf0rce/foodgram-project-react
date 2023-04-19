from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
        'password',
    ]
    email = models.EmailField(
        max_length=200,
        unique=True,
        verbose_name='E-mail адрес'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        CustomUser,
        related_name='follower',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        CustomUser,
        related_name='following',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            UniqueConstraint(
                fields=('author', 'user',),
                name='unique_follow',
            )
        ]

    def __str__(self) -> str:
        return f'{self.user} подписался на {self.author}'
