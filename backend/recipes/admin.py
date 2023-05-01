from django.contrib import admin
from recipes.models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                            ShoppingCart, Tag)


class IngridientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    search_fields = ('name',)


class RecipeIngridientAdmin(admin.ModelAdmin):
    fields = ('ingridient', 'recipe', 'amount',)
    search_fields = ('ingridient', 'recipe',)


class RecipeIngridientInline(admin.TabularInline):
    model = RecipeIngredient
    min_num = 1
    extra = 0


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug',)
    search_fields = ('name',)


class RecipeAdmin(admin.ModelAdmin):

    def number_of_additions_to_favorites(self, obj):
        return Favorite.objects.filter(recipe=obj).count()

    number_of_additions_to_favorites.short_description = (
        'Добавлений в избранное'
    )

    list_display = (
        'name',
        'author',
        'pub_date',
        'number_of_additions_to_favorites',
    )
    search_fields = ('name',)
    filter_horizontal = ('tags',)
    list_filter = ('tags', 'author',)
    autocomplete_fields = ('ingredients',)
    inlines = (RecipeIngridientInline,)
    readonly_fields = ('number_of_additions_to_favorites',)

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Ingredient, IngridientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngridientAdmin)
admin.site.register(ShoppingCart)
admin.site.register(Favorite)
