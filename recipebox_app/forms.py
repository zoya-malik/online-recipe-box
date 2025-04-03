from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Recipe, Ingredient, Folder, Review, Tag, ShoppingList

class ClientRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        user.is_admin = False
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'instructions', 'image', 'cook_time', 'avg_rating']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['recipe', 'rating', 'comment']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ['name']

