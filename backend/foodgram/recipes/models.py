from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

User = get_user_model()


class Ingridient(models.Model):
    """Модель ингридиентов."""
    name = models.CharField(
        'Наименование ингридиента',
        max_length=200,
    )
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=200,
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ('id',)
    
    def __str__(self) -> str:
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):
    """Модель тегов."""
    name = models.CharField(
        'Название',
        max_length=200,
    )
    color = models.CharField(
        'Цвет в HEX',
        help_text=(
            'Введите цвет в шестнадцатиричном формате(HEX)'
        ),
        max_length=7,
        validators=(
            RegexValidator(
                regex='^#[A-F0-9]{6}$',
                error_messages='Неверный формат цвета',
            )
        ),
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('id',)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    """Модель рецептов."""
    author = models.ForeignKey(
        'Автор рецепта',
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
    name = models.CharField(
        'Название рецепта',
        max_length=200,
    )
    text = models.TextField(
        'Описание рецепта',
    )
    ingridients = models.ManyToManyField(
        'Ингридиенты для рецепта',
        Ingridient,
        through='RecipeIngridients',
        related_name='recipes',
    )
    tags = models.ManyToManyField(
        'Теги рецепта',
        Tag,
        through='RecipeTags',
        related_name='recipes',
    )
    pub_date = models.DateTimeField(
        'Дата публикации рецепта',
        auto_now_add=True,
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления(в минутах)',
        validators=(
            MinValueValidator(
                1,
                message='Должно быть больше 0!')
        )
    )
    image = models.ImageField(
        'Фотография рецепта',
        upload_to='recipes/',
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return self.name


class RecipeIngridients(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe',
    )
    ingridients = models.ForeignKey(
        Ingridient,
        on_delete=models.CASCADE,
        related_name='ingridient',
    )

    class Meta:
        verbose_name = 'Ингридиент рецепта'
        verbose_name_plural = 'Ингридиенты рецепта'
        constraints = models.UniqueConstraint(
            fields=('recipe', 'ingridients',),
            name='unique_recipe_ingridients',
        )

    def __str__(self) -> str:
        return f'Ингридиенты для {self.recipe}: {self.ingridients}'


class RecipeTags:
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe',
    )
    tags = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='tags'
    )

    class Meta:
        verbose_name = 'Тег рецепта'
        verbose_name_plural = 'Теги рецепта'
        constraints = models.UniqueConstraint(
            fields=('recipe', 'tags',),
            name='unique_recipe_tags',
        )

    def __str__(self) -> str:
        return f'Теги для {self.recipe}: {self.tags}'


class Favorites(models.Model):
    """Модель избранного."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
    )

    class Meta:
        verbose_name = 'Избранное'
        constraints = models.UniqueConstraint(
            fields=('user', 'recipe'),
            name='unique_favorite_recipe',
        )

    def __str__(self) -> str:
        return f'{self.recipe} добавлен в избранное {self.user}'


class ShoppingList(models.Model):
    """Модель списка покупок."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_list',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_list',
    )

    class Meta:
        verbose_name = 'Список покупок'
        constraints = models.UniqueConstraint(
            fields=('user', 'recipe',),
            name='unique_shoppint_list',
        )

    def __str__(self) -> str:
        return f'{self.recipe} добавлен в список покупок {self.user}'
