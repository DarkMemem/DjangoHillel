from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm

from .models import Profile


class AccountRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class AccountUpdateForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class AccountUpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'interests']
