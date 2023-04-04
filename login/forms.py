from django import forms
from login.models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['id', 'user_name', 'passwd']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'passwd': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'id': '유저 ID',
            'user_name': '표시명',
            'passwd': '비밀번호',
        }

