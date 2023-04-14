from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class SignupForm(UserCreationForm):
    CHOICE_GENDER = (
        ('man', '남자'),
        ('woman', '여자')
    )
    email = forms.EmailField(label='아이디')
    name = forms.CharField(max_length=10, label='이름')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    alias = forms.CharField(max_length=50, label='닉네임')
    gender = forms.CharField(label='성별', widget=forms.Select(choices=CHOICE_GENDER))
    profile_img = forms.ImageField(label='프로필 이미지(선택)', widget=forms.ClearableFileInput(), required=False)
    cover_img = forms.ImageField(label='커퍼 이미지(선택)', widget=forms.ClearableFileInput(), required=False)
    introduce = forms.CharField(label='자기소개', widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2', 'alias',
                  'gender', 'profile_img', 'cover_img', 'introduce']


    def __init__(self, *args, **kwargs):
        # SignupForm 을 재정의하여 모든 template class 속성을 'form-control' 로 지정
        super(SignupForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'