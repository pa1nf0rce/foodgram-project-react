from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Exists, OuterRef, UniqueConstraint


class SubscribeQuerySet(models.QuerySet):
    def add_user_annotations(self, user_id):
        return self.annotate(
            is_subscribed=Exists(
                Subscribe.objects.filter(
                    user_id=user_id, author__pk=OuterRef('pk')
                )
            ),
        )


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

    objects = SubscribeQuerySet.as_manager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        CustomUser,
        related_name='subscriber',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        CustomUser,
        related_name='subscribing',
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
