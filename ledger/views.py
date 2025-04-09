from django.shortcuts import render, redirect
from .models import Recipe, Profile
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm

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

@login_required
def recipe_add(request):
    recipe_form = RecipeForm()

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = Profile.objects.get(user=request.user)
            recipe.save()
            return redirect('recipe_add')

   
    ctx = {'recipe_form': recipe_form}

    return render(request, 'recipe_add.html', ctx)