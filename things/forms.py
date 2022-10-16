"""Forms of the project."""

# Create your forms here.

from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(label='name', max_length=35)
    description = forms.Textarea(label='description')
    qantity = forms.NumberInput(label='quantity', min='0', max='50')