from django import forms
from .models import Comment

# forms framework - validate itself, and also easily render data
# two types Form - allows you to build standard form
# models Form - allows you to build form to create or update model instances


class EmailPostForm(forms.Form):

    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment # will automatically build a form from Comment Model
        fields = ('name', 'email', 'body') # which field you want to display, leave blank if you want to display all

class SearchForm(forms.Form):
    query = forms.CharField()
