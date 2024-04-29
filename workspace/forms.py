from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth.models import User

from news.models import News


#
# class NewsForm(forms.Form):
#     name = forms.CharField(label='Заголовок', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}))
#     image = forms.ImageField(label='Изображение', widget=forms.FileInput(
#         attrs={'accept': 'image/*', 'class': 'form-control'}))
#     description = forms.CharField(label='Краткое описание', widget=forms.Textarea(
#         attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}))
#     content = forms.CharField(label='Контент', widget=forms.Textarea(
#         attrs={'class': 'form-control', 'placeholder': 'Контент'}))
#     is_published = forms.BooleanField(label='Публичность', widget=forms.CheckboxInput())
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
#                                       empty_label='Выберите категорию',
#                                       widget=forms.Select(attrs={'class': 'form-select'}))
#     tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())


class NewsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'

    class Meta:
        model = News
        fields = [
            'name',
            'image',
            'description',
            'content',
            'is_published',
            'category',
            'tags'
        ]

        # labels = {
        #     'name': 'Custom name label'
        # }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'image': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Контент'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.CheckboxSelectMultiple()
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter password'}))


class RegisterForm(BaseUserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Придумайте пароль'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'})

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Придумайте имя пользователя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите эл. почту'}),
        }


class ChangeProfileForm(forms.ModelForm):

    # email = forms.EmailField(label='Эл. почта', required=True,
    #                          widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите эл. почту'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите эл. почту'})
        }
