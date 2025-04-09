from django.urls import path, include
from .views import recipes_list, recipe_detail, recipe_add
urlpatterns = [
    path('recipes/list', recipes_list, name='recipes_list'),
    path('recipe/<int:recipes_id>', recipe_detail, name='recipe_detail'),
    path('recipe/add', recipe_add, name='recipe_add'),
]
