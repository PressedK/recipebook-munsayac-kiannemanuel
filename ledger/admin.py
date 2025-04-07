from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage   
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class RecipeImageInline(admin.TabularInline):  
    model = RecipeImage 

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeImageInline,]
    search_fields = ('name', )
    
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name', )
    
class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('recipe', 'ingredient', 'Quantity' )
    list_display = ('recipe', 'ingredient', 'Quantity' )
    list_filter = ('recipe', 'ingredient', 'Quantity' )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
