from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ClientRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # Ensure this user is marked as client
        user.is_client = True
        user.is_admin = False  # Make sure it's not an admin
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

