from .models import Articles
from django.forms import ModelForm, TextInput, DateInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'story', 'data']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название фильма'
            }),
            "story": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "data": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выхода фильма'
            })
        }