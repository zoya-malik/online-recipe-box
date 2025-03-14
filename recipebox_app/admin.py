from django.contrib import admin
from .models import CustomUser, Recipe, Ingredient, RecipeLibrary, Folder, Review, Tag, ShoppingList

admin.site.register(CustomUser)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeLibrary)
admin.site.register(Folder)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(ShoppingList)

