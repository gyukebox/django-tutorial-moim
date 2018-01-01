from django import forms
from moim.models import MoimModel


class MoimForm(forms.ModelForm):
    class Meta:
        model = MoimModel
        exclude = ['creator', 'attendees']
