from django.contrib import admin
from .models import News, Category, Tag, AdditionalNewsInfo
from django.utils.safestring import mark_safe


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'date', 'is_published', 'get_image')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'content')
    list_filter = ('category', 'date', 'is_published', 'tags')
    readonly_fields = ('date', 'get_full_image')
    # filter_vertical = ('tags',)
    filter_horizontal = ('tags',)
    # raw_id_fields = ('category',)

    @admin.display(description='Изображение')
    def get_image(self, news: News):
        return mark_safe(f'<img src="{news.image.url}" width="150px">')

    @admin.display(description='Изображение')
    def get_full_image(self, news: News):
        return mark_safe(f'<img src="{news.image.url}" width="50%">')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(AdditionalNewsInfo)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_name', 'email', 'rating')
    list_display_links = ('id', 'news_name')
    search_fields = ('news__name', 'news__description', 'news__content')
    list_filter = ('news', 'news__category', 'news__date', 'news__tags')
    readonly_fields = ('news_name',)

    @admin.display(description='Название')
    def news_name(self, info: AdditionalNewsInfo):
        return f'{info.news.name}'

# Register your models here.
