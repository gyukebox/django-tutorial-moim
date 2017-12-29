from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='이메일')
    password = forms.CharField(widget=forms.PasswordInput(), label='비밀번호')


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=50, label='성명')
    email = forms.EmailField(label='이메일')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(), label='비밀번호')
    password_again = forms.CharField(max_length=100, widget=forms.PasswordInput(), label='비밀번호 재입력')
    age = forms.IntegerField(label='나이')
    gender = forms.CharField(label='성별')
