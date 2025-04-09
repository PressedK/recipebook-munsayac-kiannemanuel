from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Recipe, Profile
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, RecipeImageForm

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
def add_image_recipe_detail(request, recipes_id):
    recipe = Recipe.objects.get(id=recipes_id)
    recipeimage_form = RecipeImageForm()

    if request.method == 'POST':
        recipeimage_form = RecipeImageForm(request.POST, request.FILES)
       
        if recipeimage_form.is_valid():
            
            recipe_image = recipeimage_form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()

            recipe.updated_on = timezone.now()
            recipe.save()
            
            return redirect(f'/recipe/{recipes_id}')
    ctx = {
        'recipeimage_form': recipeimage_form,
        'recipe': recipe
    }
    return render(request, 'add_image_recipe_detail.html', ctx)

@login_required
def recipe_add(request):
    recipe_form = RecipeForm()
    ingredient_form = IngredientForm()
    recipeingredient_form = RecipeIngredientForm()

    if request.method == 'POST':
        
        if 'recipe_submit' in request.POST:
            recipe_form = RecipeForm(request.POST)
           
            if recipe_form.is_valid():
                recipe = recipe_form.save(commit=False)
                recipe.author = Profile.objects.get(user=request.user)
                recipe.save()
                return redirect('recipe_add')
        
        elif 'ingredient_submit' in request.POST:
            ingredient_form = IngredientForm(request.POST)

            if ingredient_form.is_valid():
                ingredient = ingredient_form.save()
                ingredient.save()
                return redirect('recipe_add')
            
        elif 'recipeingredient_submit' in request.POST:
            recipeingredient_form = RecipeIngredientForm(request.POST)

            if recipeingredient_form.is_valid():
                recipeingredient = recipeingredient_form.save()
                recipeingredient.save()

                recipe = recipeingredient.recipe
                recipe.updated_on = timezone.now()
                recipe.save()
                return redirect('recipe_add')
               
    ctx = {'recipe_form': recipe_form, 
           'ingredient_form': ingredient_form,
           'recipeingredient_form': recipeingredient_form}

    return render(request, 'recipe_add.html', ctx)