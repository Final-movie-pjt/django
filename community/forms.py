from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'rank', 'content']


class CommentForm(forms.ModelForm):
    content = forms.CharField(label=False)
    class Meta:
        model = Comment
        exclude = ['review', 'user']