from django import forms
from user_auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.auth import authenticate


class UserCreationForm(forms.ModelForm):
    username = forms.RegexField(label='用户名', max_length=30, regex=r'^[\w.@+-_]+$', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '用户名', 'required': '', 'autofocus':''},
    ), )
    email = forms.EmailField(label='邮箱',widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': '邮箱', 'required': ''}
    ), error_messages={'required': "密码不能为空"})

    password1 = forms.CharField(label='密码',widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '密码', 'required': ''}
    ),
                            )
    password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '确认密码', 'required': ''}),
                                )

    class Meta:
        model = User
        fields =['username', 'email']

    def clean_username(self):
        username = self.cleaned_data["username"]
        print('hello')
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('用户名已存在')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('密码和确认密码不一致')
        return password2

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("email已存在")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class PasswordResetForm(forms.Form):
    username = forms.RegexField(max_length=30, regex=r'^[\w.@+-_]+$',
                                error_messages={
                                    'invalid': "请输入数字,字母或常见字符",
                                    'required': "密码不能为空"
                                })
    email = forms.EmailField(error_messages={
        'invalid':"email格式错误",
        'required':"email不能为空"
    })

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if username and email:
            try:
                self.user = User.objects.get(username=username, email=email, is_active=True)
            except User.DoesNotExist:
                raise forms.ValidationError("此用户名不存在或用户名与email不匹配")
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width:20', 'placeholder': '用户名', 'required': '', 'autofocus': ''}
    ), error_messages={'required': "用户名不能为空"},
                               )

    password = forms.CharField(label='密码', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '密码', 'required': ''}
    ), error_messages={'required': "密码不能为空"},)

    auto_login = forms.BooleanField(label='记住密码', required=False, widget=forms.CheckboxInput(
        attrs={'value': 1}
    ))

    def __init__(self,request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        self.auto_login = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        auto_login = self.cleaned_data.get('auto_login',None)

        if username and password:
            if not User.objects.filter(username=username).exists():
                raise forms.ValidationError("该账号不存在")

            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('账号或密码错误')

        if auto_login:
            self.auto_login = True

        return self.cleaned_data

    def get_user(self):
        return self.user_cache

    def get_auto_login(self):
        """是否勾选了自动登录"""
        return self.auth_login





