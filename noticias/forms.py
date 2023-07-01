from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import usuario

class UsusarioForm(ModelForm):

    class Meta:
        model=usuario
        field = '__all__'