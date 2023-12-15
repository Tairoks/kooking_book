from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipesListView.as_view(), name='recipes'),
    path('<slug:recipe_slug>', views.recipe_info, name='recipe_info'),
    path('favourites/', views.favourite_list, name='favourites_list'),
    path('fav/<int:recipe_id>', views.favourite_add, name='favourite'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('search/', views.search_recipe, name='search_recipe'),
    path('delete/<int:get_recipe>', views.recipe_delete, name='delete_recipe'),
    path('edit/<int:recipe_id>', views.edit_recipe, name='edit_recipe'),
    ]
