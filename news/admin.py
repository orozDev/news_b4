from django.contrib import admin
from .models import News, Category, Tag, AdditionalNewsInfo, NewsAttribute
from django.utils.safestring import mark_safe


class NewsAttributeStackedInline(admin.StackedInline):
    model = NewsAttribute
    extra = 1


class AdditionalNewsInfoTabularInline(admin.TabularInline):
    model = AdditionalNewsInfo


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
    inlines = (NewsAttributeStackedInline, AdditionalNewsInfoTabularInline)

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


# Register your models here.
