from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='recipes'),
    path('recipes/', views.text_recipes)
    ]
