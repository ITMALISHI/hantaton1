from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class myUserCreationForm(UserCreationForm):
    username = forms.RegexField(
        max_length=30,
        regex=r"^[\w.@+-]+$",
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},

        widget=forms.TextInput(attrs={'class': 'form-control',
                                'required': 'true',
                                'placeholder': 'Никнейм',
                                      'id': 'nameRegister'
                                })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'required': 'true',
                                            'placeholder': 'Пароль',
                                          'id': "passwordRegister",
                                          })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'password',
                                          'required': 'true',
                                          'placeholder': 'Повторите пароль',
                                            'id': "passwordRegister"
                                          }),
    )

    email = forms.CharField(
        label=("Email"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'email',
                                      'placeholder': 'Email',
                                      'required': 'true',
                                      'id': "emaiRegister"
                                      })
    )

    class Meta:
        model = User
        fields=('username', 'password1', 'password2', 'email')