from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, 'recipes_list.html', ctx)

def recipe_detail(request, recipes_id):
    recipe = Recipe.objects.get(id=recipes_id)
    ctx = {
        'recipe': recipe
    }
    return render(request, 'recipe_detail.html', ctx)

