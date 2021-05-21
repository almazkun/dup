from django import forms

from dup.models import Website


class WebsiteForm(forms.ModelForm):
    
    class Meta:
        model = Website
        fields = ("url",)
