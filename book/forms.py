from django import forms
from .models import Recipes, Ingredients


# class IngredientsAdd(forms.Select):
#     def create_option(
#             self, name, value, label, selected, index, subindex=None, attrs=None
#     ):
#         option = super().create_option(
#             name, value, label, selected, index, subindex, attrs
#         )
#         if value:
#             option["attrs"]["quantity"] = value.instance.quantity
#             option["attrs"]["type"] = value.instance.type
#             option["attrs"]["title"] = value.instance.title
#         return option


class AddRecipe(forms.ModelForm):
    """Form for adding and editing a recipe"""
    class Meta:
        model = Recipes
        fields = ["title", "photo", "ingredients", "cooking", "creator", "time_cook"]
        widgets = {
            "creator": forms.HiddenInput()
        }


class SearchForm(forms.Form):
    """Recipe search form"""
    title = forms.CharField(max_length=100)
