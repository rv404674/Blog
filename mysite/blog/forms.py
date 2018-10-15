from django import forms

# forms framework - validate itself, and also easily render data
# two types Form - allows you to build standard form
# models Form - allows you to build form to create or update model instances


class EmailPostForm(forms.Form):

    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
