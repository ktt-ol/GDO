from django import forms
from .models import *


class keyForm(forms.ModelForm):

    class Meta:
        model = key
        fields = ('description', 'valid_from', 'valid_to', 'valid_for', 'active', 'created_by')



#class groupForm(forms.ModelForm):
