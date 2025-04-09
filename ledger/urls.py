from django.urls import path, include
from .views import recipes_list, recipe_detail, recipe_add, add_image_recipe_detail
urlpatterns = [
    path('recipes/list', recipes_list, name='recipes_list'),
    path('recipe/<int:recipes_id>', recipe_detail, name='recipe_detail'),
    path('recipe/add', recipe_add, name='recipe_add'),
    path('recipe/<int:recipes_id>/add_image', add_image_recipe_detail, name='add_image_recipe_detail'),
]
