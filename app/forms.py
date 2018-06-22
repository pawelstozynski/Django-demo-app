from django import forms

from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Type name'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type content'}),
        }


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Create todo'})
        }