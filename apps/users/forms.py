from django.contrib.auth.forms import UserCreationForm
from apps.main.models import User
from apps.yandex.models import Device
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")


class ConnectForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__' 