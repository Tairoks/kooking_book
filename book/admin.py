from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Ingredients, Recipes


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height"110">')

    get_image.short_description = "Photo"


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ("title",)
