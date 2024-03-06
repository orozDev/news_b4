from django.contrib import admin
from .models import News, Category, Tag

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)

# Register your models here.
