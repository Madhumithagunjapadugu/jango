from django import forms
from newapp.models import schl

class schl_form(forms.ModelForm):
    class Meta:
        model='schl'
        fields='__all__'
        