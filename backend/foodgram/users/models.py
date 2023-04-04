from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Кастомная модель пользователя."""
    email = models.EmailField(
        'Адрес электронной почты',
        max_length=254,
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = (
            models.UniqueConstraint(
                fields=('username', 'email',),
                name='unique_username_email'
            ),
        )

    def __str__(self) -> str:
        return self.username
