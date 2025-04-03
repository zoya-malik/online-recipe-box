from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model with added roles for admin and client.
    """
    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Tag(models.Model):
    """
    Tag model to categorize recipes and folders.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    """
    Ingredient model to specify ingredients used in recipes.
    """
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    """
    Recipe model containing instructions, image, cook time, and average rating.
    Can have multiple tags and ingredients.
    """
    title = models.CharField(max_length=255)
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    cook_time = models.IntegerField()
    avg_rating = models.FloatField(default=0.0)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    tags = models.ManyToManyField(Tag, related_name='recipes')

    def __str__(self):
        return self.title

class Review(models.Model):
    """
    Review model for clients to leave reviews on recipes.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.recipe.title}"

class Folder(models.Model):
    """
    Folder model for organizing recipes in the library.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, related_name='folders')

    def __str__(self):
        return self.name

class RecipeLibrary(models.Model):
    """
    Recipe library for saving user-specific recipes.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Library"

class ShoppingList(models.Model):
    """
    Shopping list model associated with a user and containing ingredients.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient, related_name='shopping_lists')

    def __str__(self):
        return self.name

