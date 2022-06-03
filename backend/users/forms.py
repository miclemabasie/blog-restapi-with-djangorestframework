from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    class meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"