from django import forms
from core.models import Ad, CategoriesAd, Comment
from django.contrib.auth.forms import (
    AuthenticationForm, UsernameField, UserCreationForm
)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль', 'class': 'form-control'
        })
    )

    password2 = forms.CharField(
        label='Подтверждение пароля',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Подтвердите пароль', 'class': 'form-control'
        }),
        help_text="Повторите ввод пароля"
    )

    class Meta:
        model = User
        fields = ('email', 'username')
        widgets = {
            'username' : forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Email', 
                'authofocus': True
            }),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
            'autofocus' : True, 'placeholder': 'Username', 'class': 'form-control'
    }))

    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль', 'class': 'form-control'
    }))

    error_messages = {
        'invalid_login': 'Введен неправильный логин или пароль'
    }


class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        categories = forms.ModelChoiceField(
            queryset=CategoriesAd.objects.all(), empty_label=None, to_field_name = 'Категории'
        )
   
        fields = ['heading', 'categories', 'description', 'price', 'image']
        labels = {
            'heading': 'Заголовок объявления',
            'categories': 'Категория объявления',
            'description': 'Описание объявления',
            'categories': 'Категория объявления',
            'price': 'Цена',
            'image': 'Выберите файл',
        }
       
        widgets = {
            'heading' : forms.Textarea(attrs={
                'class': 'form-control', 'placeholer' : 'Заголовок объявления'
            }),
            'description' : forms.Textarea(attrs={
                'class': 'form-control', 'placeholer' : 'Описание объявления'
            }),
            'price' : forms.Textarea(attrs={
                'class': 'form-control', 'placeholer' : 'Цена'
            }),
            'image' : forms.ClearableFileInput(attrs={
                'type': 'file', 'class' : 'form-control-file'
            }),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Оставьте комментарий'
        }

        widget = {
            'text' : forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': ' Текст комментария'
            }),
        }