# Generated by Django 2.2.16 on 2023-04-18 01:43

from django.db import migrations


INITIAL_TAGS = [
    {'color': '#32CD32', 'name': 'Завтрак', 'slug': 'breakfast'},
    {'color': '#8B8970', 'name': 'Обед', 'slug': 'lunch'},
    {'color': '#0000FF', 'name': 'Ужин', 'slug': 'dinner'},
    {'color': '#00EEEE', 'name': 'Перекус', 'slug': 'snack'},
    {'color': '#FF00FF', 'name': 'Десерт', 'slug': 'dessert'},
]

def add_tags(apps, schema_editor):
    Tag = apps.get_model('recipes', 'Tag')
    for tag in INITIAL_TAGS:
        new_tag = Tag(**tag)
        new_tag.save()


def remove_tags(apps, schema_editor):
    Tag = apps.get_model('recipes', 'Tag')
    for tag in INITIAL_TAGS:
        Tag.objects.get(slug=tag['slug']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20230418_0435'),
    ]

    operations = [
        migrations.RunPython(
            add_tags,
            remove_tags
        )
    ]
