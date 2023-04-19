# Generated by Django 2.2.16 on 2023-04-19 21:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_add_ingredients'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'verbose_name': 'Избранное', 'verbose_name_plural': 'Избранное'},
        ),
        migrations.AlterModelOptions(
            name='recipeingridient',
            options={'verbose_name': 'Ингредиенты в рецепте', 'verbose_name_plural': 'Ингредиенты в рецепте'},
        ),
        migrations.AlterField(
            model_name='recipeingridient',
            name='amount',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Должно быть больше 0!')], verbose_name='Количество ингридиента'),
        ),
        migrations.AlterField(
            model_name='recipeingridient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingridient_list', to='recipes.Recipe'),
        ),
    ]
