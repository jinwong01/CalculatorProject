
from .models import Calculation
from django import forms
from .models import Calculation

class CalculationForm(forms.ModelForm):
   class Meta:
       model = Calculation
       fields = ['num_one', 'num_two', 'calculation_type']
   calculation_type = forms.IntegerField(widget=forms.Select(
     choices=[(0, "+"), (1, "-"), (2, "*"), (3, "/")]))

