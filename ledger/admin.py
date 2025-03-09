from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', )

    
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name', )
    
class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

     # Use the name to search
    search_fields = ('recipe', 'ingredient', 'Quantity' )
    # Display just the name and the due date in the list
    list_display = ('recipe', 'ingredient', 'Quantity' )
    # Enable filtering via the teacher's name and the number of units
    list_filter = ('recipe', 'ingredient', 'Quantity' )

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
