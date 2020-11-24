from django import forms
from .models import Review, Comment
from movies.models import Movies

class ReviewForm(forms.ModelForm):
    # movie_title = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'placeholder' = Movie.objects.all()
    #     })
    # )
    class Meta:
        model = Review
        fields = ['title', 'rank', 'content',]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['review', 'user']
