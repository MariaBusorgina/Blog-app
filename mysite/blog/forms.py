from django import forms

from .models import Comment


class EmailPostForm(forms.Form):
    """Форма для отправки публикации по email"""
    name = forms.CharField(max_length=25, label='Имя')
    email = forms.EmailField()
    to = forms.EmailField(label='Кому')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='Комментарии')


class CommentForm(forms.ModelForm):
    """Форма для комментариев"""
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class SearchForm(forms.Form):
    """Форма для поиска по запросу"""
    query = forms.CharField(label='Введите запрос')