from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    cook_time = models.IntegerField()
    avg_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RecipeLibrary(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Library"

class Folder(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.recipe.title}"

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ShoppingList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

