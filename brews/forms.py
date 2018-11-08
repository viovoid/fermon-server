from django import forms

from .models import Brew, Update

class BrewForm(forms.ModelForm):

  class Meta:
    model = Brew
    fields = ('ident', 'category', 'init_date', 'ingredients')

class UpdateForm(forms.ModelForm):

  class Meta:
    model = Update
    fields = ('post_date', 'body')
