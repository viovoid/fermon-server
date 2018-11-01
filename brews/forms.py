from django import forms

from .models import Brew

class BrewForm(forms.ModelForm):

  class Meta:
    model = Brew
    fields = ('ident', 'category', 'init_date', 'ingredients')
