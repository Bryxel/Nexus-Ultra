from django import forms
from .models import Snippet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full rounded-lg border border-gray-300 shadow-sm focus:border-black focus:ring-1 focus:ring-black focus:outline-none px-4 py-3 text-lg'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 shadow-sm focus:border-black focus:ring-1 focus:ring-black focus:outline-none px-4 py-3 text-lg'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password_widget_attrs = {
            'class': 'w-full rounded-lg border border-gray-300 shadow-sm focus:border-black focus:ring-1 focus:ring-black focus:outline-none px-4 py-3 text-lg'
        }
        self.fields['password1'].widget.attrs.update(password_widget_attrs)
        self.fields['password2'].widget.attrs.update(password_widget_attrs)

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full rounded-md border-gray-300 shadow-sm focus:border-black focus:ring-1 focus:ring-black focus:outline-none px-4 py-3',
                'placeholder': 'Code Snippet Title'
            }),
            'code': forms.Textarea(attrs={
                'rows': 10,
                'class': 'w-full rounded-md border-gray-300 shadow-sm focus:border-black focus:ring-1 focus:ring-black focus:outline-none font-mono px-4 py-3',
                'placeholder': 'Paste your code here...'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'w-full rounded-md border-gray-300 shadow-sm focus:border-black focus:ring-1 focus:ring-black focus:outline-none px-4 py-3',
                'placeholder': 'e.g., python, django, web'
            })
        }
