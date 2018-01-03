from django import forms
from django.contrib.auth.password_validation import validate_password


class LoginForm(forms.Form):
    email = forms.EmailField(label='이메일')
    password = forms.CharField(widget=forms.PasswordInput(), label='비밀번호')


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=50, label='성명')
    email = forms.EmailField(label='이메일')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
    ), label='비밀번호', validators=[validate_password, ])
    password_again = forms.CharField(max_length=100, widget=forms.PasswordInput(
    ), label='비밀번호 재입력', validators=[validate_password, ])
    age = forms.IntegerField(label='나이')
    gender = forms.CharField(label='성별')

    def is_valid(self):
        if super(RegisterForm, self).is_valid() is False:
            return False

        data = self.cleaned_data

        if data['password'] != data['password_again']:
            return False

        if data['gender'] != 'M' and data['gender'] != 'W':
            return False

        return True
