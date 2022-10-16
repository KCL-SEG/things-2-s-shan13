"""Forms of the project."""

# Create your forms here.
from .models import Thing
from django import forms

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea()}