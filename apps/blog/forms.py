from django.forms import forms
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class EmailForm(forms.Form):
    subject = forms.CharField(label='Введите имя ', max_length=50)

    message = forms.CharField(label='Укажите номер в сообщении  ', widget=forms.Textarea)
    # to_emails = forms.CharField(max_length=100, initial='cliclinick@gmail.com', required=False)