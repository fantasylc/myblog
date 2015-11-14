from django import forms
from captcha.fields import CaptchaField
from .models import Leavemessage


class MessageForm(forms.ModelForm):
    message = forms.CharField(label='留言',widget=forms.Textarea(
       attrs={'class':'form-control message_text','placeholder':'留个言吧','required':''}
    ),error_messages={'required':'留言不能为空'})
    name = forms.CharField(label='留个名吧',max_length=30,widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '姓名', 'required': '',}
    ), error_messages={'required': "用户名不能为空"})
    captcha = CaptchaField(label='验证码')

    class Meta:
        model = Leavemessage
        fields = ['name', 'message']

