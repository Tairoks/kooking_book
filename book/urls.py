from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_views, name='recipes'),
    path('<slug:recipe_slug>', views.recipe_info, name='recipe_info'),
    path('favourites/', views.favourite_list, name='favourites_list'),
    path('fav/<int:recipe_id>', views.favourite_add, name='favourite'),
    path('add/', views.add_recipe, name='add_recipe'),
    ]
