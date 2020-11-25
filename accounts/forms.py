from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '아이디를 입력해주세요',
        })
    )
    password1 = forms.CharField(
    label='비밀번호',
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '비밀번호를 입력해주세요',
        
        })
    )
    password2 = forms.CharField(
    label='비밀번호 확인',
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '비밀번호를 확인해주세요',      
        })
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '아이디를 입력해주세요',
        })
    )
    password1 = forms.CharField(
    label='비밀번호',
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '비밀번호를 입력해주세요',
        
        })
    )
    password2 = forms.CharField(
    label='비밀번호 확인',
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '비밀번호를 확인해주세요',      
        })
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '아이디를 입력해주세요',
        })
    )
    password = forms.CharField(
    label='비밀번호',
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '비밀번호를 입력해주세요',
        
        })
    )
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1',)