from django import forms
from . import models

class GhostAdd(forms.ModelForm):
    class Meta:
        model = models.GhostPost
        fields = ['ghostTitle', 'body', 'is_boast']