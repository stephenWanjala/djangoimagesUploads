# forms.py
from django import forms
from .models import UploadedImage


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({
            'class': 'form-control-file'
        })
