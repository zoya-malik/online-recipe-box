# recipebox_app/views.py
from django.db.models import Q
from .models import Recipe, Ingredient, Tag
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.decorators import login_required
from .forms import (
    UserUpdateForm, ClientRegistrationForm, RecipeForm, 
    IngredientForm, FolderForm, ReviewForm, TagForm, ShoppingListForm
)
from .models import (
    Recipe, Ingredient, RecipeLibrary, Folder, 
    Review, Tag, ShoppingList, CustomUser
)

@login_required
def profile_view(request):
    """
    Display the current user's profile info.
    """
    return render(request, 'registration/profile.html')

@login_required
def profile_edit_view(request):
    """
    Allow the current user to edit their profile info.
    """
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('recipebox_app:profile')  
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'registration/profile_edit.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def client_register(request):
    """
    Allows new users to register as clients.
    Uses ClientRegistrationForm, which sets is_client=True, is_admin=False.
    """
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipebox_app:index')
    else:
        form = ClientRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    if query:
        results = Recipe.objects.filter(title__icontains=query)
    else:
        results = Recipe.objects.all()
    return render(request, 'search_results.html', {'results': results})




# Recipe Views
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe/recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe/recipe_detail.html'
    context_object_name = 'recipe'

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipe/recipe_form.html'
    fields = ['title', 'instructions', 'image', 'cook_time', 'avg_rating']
    success_url = reverse_lazy('recipebox_app:recipe-list')

class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'recipe/recipe_form.html'
    fields = ['title', 'instructions', 'image', 'cook_time', 'avg_rating']
    success_url = reverse_lazy('recipebox_app:recipe-list')

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipebox_app:recipe-list')

# Ingredient Views
class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredient/ingredient_list.html'
    context_object_name = 'ingredients'

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'ingredient/ingredient_detail.html'
    context_object_name = 'ingredient'

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = 'ingredient/ingredient_form.html'
    fields = ['name', 'quantity', 'unit']
    success_url = reverse_lazy('recipebox_app:ingredient-list')

class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = 'ingredient/ingredient_form.html'
    fields = ['name', 'quantity', 'unit']
    success_url = reverse_lazy('recipebox_app:ingredient-list')

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'ingredient/ingredient_confirm_delete.html'
    success_url = reverse_lazy('recipebox_app:ingredient-list')

# Recipe Library Views
class RecipeLibraryListView(ListView):
    model = RecipeLibrary
    template_name = 'recipelibrary/recipelibrary_list.html'
    context_object_name = 'libraries'

class RecipeLibraryDetailView(DetailView):
    model = RecipeLibrary
    template_name = 'recipelibrary/recipelibrary_detail.html'
    context_object_name = 'library'

class RecipeLibraryCreateView(CreateView):
    model = RecipeLibrary
    template_name = 'recipelibrary/recipelibrary_form.html'
    fields = ['user', 'recipe']
    success_url = reverse_lazy('recipebox_app:library-list')

class RecipeLibraryUpdateView(UpdateView):
    model = RecipeLibrary
    template_name = 'recipelibrary/recipelibrary_form.html'
    fields = ['user', 'recipe']
    success_url = reverse_lazy('recipebox_app:library-list')

class RecipeLibraryDeleteView(DeleteView):
    model = RecipeLibrary
    template_name = 'recipelibrary/recipelibrary_confirm_delete.html'
    success_url = reverse_lazy('recipebox_app:library-list')

# Folder Views
class FolderListView(ListView):
    model = Folder
    template_name = 'folder/folder_list.html'
    context_object_name = 'folders'

class FolderDetailView(DetailView):
    model = Folder
    template_name = 'folder/folder_detail.html'
    context_object_name = 'folder'

class FolderCreateView(CreateView):
    model = Folder
    template_name = 'folder/folder_form.html'
    fields = ['user', 'name']
    success_url = reverse_lazy('recipebox_app:folder-list')

class FolderUpdateView(UpdateView):
    model = Folder
    template_name = 'folder/folder_form.html'
    fields = ['user', 'name']
    success_url = reverse_lazy('recipebox_app:folder-list')

class FolderDeleteView(DeleteView):
    model = Folder
    template_name = 'folder/folder_confirm_delete.html'
    success_url = reverse_lazy('recipebox_app:folder-list')

# Review Views
class ReviewListView(ListView):
    model = Review
    template_name = 'review/review_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review/review_detail.html'
    context_object_name = 'review'

class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review/review_form.html'
    fields = ['user', 'recipe', 'rating', 'comment']
    success_url = reverse_lazy('recipebox_app:review-list')

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'review/review_form.html'
    fields = ['user', 'recipe', 'rating', 'comment']
    success_url = reverse_lazy('recipebox_app:review-list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_confirm_delete.html'
    success_url = reverse_lazy('recipebox_app:review-list')

# Tag Views
class TagListView(ListView):
    model = Tag
    template_name = 'tag/tag_list.html'
    context_object_name = 'tags'

class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag/tag_detail.html'
    context_object_name = 'tag'

class TagCreateView(CreateView):
    model = Tag
    template_name = 'tag/tag_form.html'
    fields = ['name']
    success_url = reverse_lazy('recipebox_app:tag-list')

class TagUpdateView(UpdateView):
    model = Tag
    template_name = 'tag/tag_form.html'
    fields = ['name']
    success_url = reverse_lazy('recipebox_app:tag-list')

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tag/tag_confirm_delete.html'
    success_url = reverse_lazy('recipebox_app:tag-list')

# Shopping List Views
class ShoppingListListView(ListView):
    model = ShoppingList
    template_name = 'shoppinglist/shoppinglist_list.html'
    context_object_name = 'shoppinglists'

class ShoppingListDetailView(DetailView):
    model = ShoppingList
    template_name = 'shoppinglist/shoppinglist_detail.html'
    context_object_name = 'shoppinglist'

class ShoppingListCreateView(CreateView):
    model = ShoppingList
    template_name = 'shoppinglist/shoppinglist_form.html'
    fields = ['name', 'user']
    success_url = reverse_lazy('recipebox_app:shoppinglist-list')

class ShoppingListUpdateView(UpdateView):
    model = ShoppingList
    template_name = 'shoppinglist/shoppinglist_form.html'
    fields = ['name', 'user']
    success_url = reverse_lazy('recipebox_app:shoppinglist-list')

class ShoppingListDeleteView(DeleteView):
    model = ShoppingList
    template_name = 'shoppinglist/shoppinglist_confirm_delete.html'
    success_url = reverse_lazy('recipebox_app:shoppinglist-list')
      
