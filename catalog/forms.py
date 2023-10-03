from .models import BookInstance, Book
from django import forms


class LoanBookForm(forms.ModelForm):
    """Form for a librarian to loan books."""

    class Meta:
        model = BookInstance
        fields = ('book', 'borrower',)
        widgets = {
            'book': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # Use all fields from the Book model
