from allauth.account.forms import LoginForm
from django import forms

class CustomLoginForm(LoginForm):
    remember = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only keep the username, password, and remember fields
        self.fields = {
            'login': self.fields['login'],
            'password': self.fields['password'],
            'remember': self.fields['remember'],
        }
