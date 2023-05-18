from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class Formhome(forms.Form):
    email = forms.EmailField(label=False)


class Criarcontaform(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2')


