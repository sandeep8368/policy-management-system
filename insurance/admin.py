from django.contrib import admin

# Register your models here.
from django import forms
from .models import Policy

class PolicyForm(forms.ModelForm):
    class Meta:
        class Meta:
            model = Policy
            fields = '__all__'