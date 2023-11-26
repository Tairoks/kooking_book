from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from .models import Recipes


def index(request):
    return render(request, "base.html")


def text_recipes(request):
    return render(request, "recipes.html")


def catalog_views(request):
    recipes = Recipes.objects.all()
    context ={
        "recipes": recipes
        }
    return render(request, "recipes.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h3>Page not found</h3>")
