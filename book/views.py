from django.shortcuts import render, HttpResponse , redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import Recipes
from .form import AddRecipe


def index(request):
    """Basic page"""
    return render(request, "base.html")


def recipes_views(request):
    """Function of presenting all recipes"""
    recipes = Recipes.objects.all()
    context = {
        "recipes": recipes
        }
    return render(request, "recipes.html", context=context)


def recipe_info(request, recipe_slug):
    """Recipe Information Views"""
    recipe = Recipes.objects.prefetch_related().get(slug=recipe_slug)
    ingredients = recipe.ingredients.all()
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'recipe_info.html', context=context)


def favourite_add(request, recipe_id):
    """Function of adding and removing recipes to favorites"""
    recipe = Recipes.objects.get(id=recipe_id)
    profile = request.user.profile_user
    if profile.favourites.filter(id=recipe_id).exists():
        profile.favourites.remove(recipe)
    else:
        profile.favourites.add(recipe)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favourite_list(request):
    """View of selected recipes"""
    f_recipes = request.user.profile_user.favourites.all()
    context = {
        "f_recipes": f_recipes
    }
    return render(request, 'favourites.html', context=context)


def add_recipe(request):
    if request.method == "POST":
        form = AddRecipe(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes')
    else:
        form = AddRecipe()
    return render(request, 'add_recipe.html', )


def pageNotFound(request, exception):
    """Non-existent page error function"""
    return HttpResponseNotFound("<h3>Page not found</h3>")
