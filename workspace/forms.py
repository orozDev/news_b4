from django import forms

from news.models import Category, Tag, News


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
