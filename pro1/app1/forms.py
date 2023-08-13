from django import forms
from .models import YourTask

class YourTaskForms(forms.ModelForm):
    class Meta:
        model = YourTask
        fields = ['title', 'description',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'custom-input'}),
            'description': forms.Textarea(attrs={'class': 'custom-textarea'}),
        }
