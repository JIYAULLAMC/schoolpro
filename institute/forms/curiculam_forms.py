from django import forms
from ..models import Curiculam

class CuriculamForm(forms.ModelForm):

    class Meta:
        model = Curiculam
        fields = ["cclm_id",]