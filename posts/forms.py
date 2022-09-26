from django import forms

from .models import Post


class CreatePostForm(forms.Form):
    picture = forms.ImageField(required=True)
    description = forms.CharField(widget=forms.widgets.Textarea(), required=True)
    tags = forms.CharField(widget=forms.widgets.TextInput(), required=True)









