from django import forms
from .models import Image, Reply

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'password']
        widgets = {
            'image' : forms.FileInput(attrs={'id' : 'input_image_file'}),
            'password' : forms.PasswordInput(attrs={'id' : 'input_image_password'}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['name', 'content', 'password']
        labels = {
            'name': '닉네임',
            'content': '내용',
            'password': '비밀번호',
        }