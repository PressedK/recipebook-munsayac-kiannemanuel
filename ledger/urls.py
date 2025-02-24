from django.urls import path
from .views import index, recipes_list, recipe1, recipe2 #every new page gets added here
urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipes_list, name='recipes_list'),
    path('recipe/1', recipe1, name='recipe1'),
    path('recipe/2', recipe2, name='recipe2'),
]

app_name = "ledger"
