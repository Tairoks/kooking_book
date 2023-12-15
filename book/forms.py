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
    class Meta:
        model = Recipes
        fields = ["title", "photo", "ingredients", "cooking", "creator", "time_cook"]
        widgets = {
            "creator": forms.HiddenInput()
        }

        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             "class": "form-control rounded-4",
        #             "style": "max-width: 300px",
        #             "placeholder": "Title"
        #         }),
        #     'photo': forms.FileInput(
        #         attrs={
        #             "class": "form-control rounded-4",
        #             "style": "max-width: 300px",
        #             "placeholder": "Choose file ..."
        #         }
        #     ),
        #     'ingredients': IngredientsAdd,
        #     'cooking': forms.Textarea(
        #         attrs={
        #             "class": "form-control rounded-4",
        #             "style": "max-width: 300px",
        #             "placeholder": "Cooking method"
        #         }),
        #     'time_cook': forms.TimeInput(
        #         attrs={
        #             "class": "form-control rounded-4",
        #             "style": "max-width: 300px",
        #             "placeholder": "Cooking time"
        #         }),
        # }


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100)
