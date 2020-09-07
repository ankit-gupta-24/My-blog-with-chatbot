from django.forms import ModelForm
from django import forms
from .models import ArticleComment

class CommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['comment_description']
        widgets = {
            'comment_description':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Leave a comment'
                }
            )
        }