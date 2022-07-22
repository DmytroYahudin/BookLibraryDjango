from django import forms

from .models import Author, Book, Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["comment"]
        labels = {"comment": ""}
        widgets = {"comment": forms.Textarea(attrs={"cols": 20, "rows": 2})}


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ["number_of_views"]
