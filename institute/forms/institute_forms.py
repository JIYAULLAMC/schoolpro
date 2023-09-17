from ..models import Institute
from django import forms
from institute.consts import CURCULAM_CATEGORY

class InstituteForm(forms.ModelForm):
    
    class Meta:
        model = Institute
        fields = "__all__"
