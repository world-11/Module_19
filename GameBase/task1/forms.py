from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите ')
    password = forms.CharField(max_length=8, label='Введите пароль')
    password_ = forms.CharField(max_length=8, label='Подтвердите пароль')
    age = forms.CharField(max_length=3, label='Введите возраст')

