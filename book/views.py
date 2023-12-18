import logging

from django.shortcuts import render, HttpResponse , redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView
from .models import Recipes, Ingredients
from .forms import AddRecipe, SearchForm


logger = logging.getLogger('recipe_logger')


def index(request):
    """Basic page"""
    return render(request, "base.html")


class RecipesListView(ListView):
    """model representation class Recipes"""
    model = Recipes
    template_name = "recipes.html"
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipes.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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
    """Add recipe function"""
    form = AddRecipe()
    if request.method == "POST":
        form = AddRecipe(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.save()
            logger.info(f"Recipe {obj.title} created by {request.user}")
            return redirect('recipes')
    context = {
        'form': form
    }
    return render(request, "add_recipe.html", context=context)


def recipe_delete(request, get_recipe):
    """Button to delete a recipe"""
    recipe = Recipes.objects.get(id=get_recipe)
    recipe.delete()
    logger.info(f"Recipe by {recipe.creator} removed {recipe.title}")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def edit_recipe(request, recipe_id):
    """Button to edit recipe"""
    form = Recipes.objects.get(id=recipe_id)
    form_ = AddRecipe(request.POST, instance=form)
    if request.method == "POST":
        if form_.is_valid():
            obj = form_.save(commit=False)
            obj.creator = request.user
            obj.save()
            form_.save_m2m()
            logger.info(f"Recipe {obj.title} edited {request.user}")
            return redirect('recipes')
    context = {
        'form': form_
    }
    return render(request, "edit_recipe.html", context=context)


def search_recipe(request):
    """Search recipes by name"""
    query = request.GET.get('q')
    recipes = Recipes.objects.filter(title__icontains=query)
    context = {
        "recipes": recipes
    }

    return render(request, "search_recipe.html", context=context)


def pageNotFound(request, exception):
    """Non-existent page error function"""
    return HttpResponseNotFound("<h3>Page not found</h3>")
