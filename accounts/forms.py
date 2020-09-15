from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import Profile


User = get_user_model()


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': '아이디를 입력해주세요.'})
        self.fields['password1'].widget.attrs.update({'placeholder': '비밀번호를 입력해주세요.'})
        self.fields['password2'].widget.attrs.update({'placeholder': '비밀번호를 다시 입력해주세요.'})

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nickname"]
        widgets = {
            'nickname': forms.TextInput(attrs={'placeholder': '닉네임을 입력해주세요.'})
        }