from django.db import models
from django.urls import reverse
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_detail", args=[str(self.id)])

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,  related_name = 'ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name = 'recipe')
    Quantity = models.CharField(max_length = 255)

    