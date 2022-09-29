from django.forms import ModelForm
from django import forms
from seuapp.models import Usuario

# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha', 'nome', 'ultimo_nome']