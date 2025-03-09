from django.db import models

# Create your models here.

class Ingredient(models.Models)
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient_name", args=[self.name])

class Recipe(models.Models)
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_name", args=[self.name])

class RecipeIngredient(models.Models)
    Quantity = models.CharField(max_length = 255)
    ingredient = models.ForeignKey(
                        Ingredient, 
                        on_delete=models.CASCADE, 
                        related_name = 'ingredients'
    )
    recipe = models.ForeignKey(
                        Recipe, 
                        on_delete=models.CASCADE, 
                        related_name = 'recipe'
    )



