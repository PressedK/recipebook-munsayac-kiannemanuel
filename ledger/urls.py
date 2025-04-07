from django.urls import path, include
from .views import recipes_list, recipe_detail
urlpatterns = [
    path('recipes/list', recipes_list, name='recipes_list'),
    path('recipe/<int:recipes_id>', recipe_detail, name='recipe_detail'),
]
