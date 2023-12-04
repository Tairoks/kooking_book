from django import forms
from .models import Recipes


class AddRecipe(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ["title", "photo", "ingredients", "cooking", "time_cook"]
