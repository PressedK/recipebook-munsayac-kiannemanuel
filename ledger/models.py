from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    bio = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length = 255)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recipes")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_detail", args=[str(self.id)])

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,  related_name = 'ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name = 'recipe')
    Quantity = models.CharField(max_length = 255)

