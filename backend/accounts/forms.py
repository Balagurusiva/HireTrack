from attr import fields
from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from accounts.models import User

class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', "first_name", "last_name")
