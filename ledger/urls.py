from django.urls import path, include
from .views import recipes_list, recipe_detail #every new page gets added here
urlpatterns = [
  
    path('recipes/list', recipes_list, name='recipes_list'),
    path('recipe/<int:recipes_id>', recipe_detail, name='recipe_detail'),
    path('accounts', include('django.contrib.auth.urls')) 
]
