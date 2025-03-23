from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required

@login_required
def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, 'recipes_list.html', ctx)

@login_required
def recipe_detail(request, recipes_id):
    recipe = Recipe.objects.get(id=recipes_id)
    ctx = {
        'recipe': recipe
    }
    return render(request, 'recipe_detail.html', ctx)