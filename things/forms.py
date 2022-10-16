"""Forms of the project."""

# Create your forms here.

from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(label='name', max_length=35)
    description = forms.CharField(widget=forms.Textarea, label='description')
    quantity = forms.CharField(widget=forms.NumberInput(attrs={'min':1, 'max':50}), label='quantity')