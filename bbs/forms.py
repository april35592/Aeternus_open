from django import forms
from .models import Guest

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'content']
        labels = {
            'name': '닉네임',
            'content': '내용',
        }