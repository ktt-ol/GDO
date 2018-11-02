from django import forms
from .models import key


class keyForm(forms.ModelForm):

    class Meta:
        model = key
        fields = ('description', 'valid_from', 'valid_to', 'valid_for', 'active')



#class groupForm(forms.ModelForm):
