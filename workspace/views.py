from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from news.models import News, Category, Tag


def workspace(request):
    news = News.objects.all().order_by('-date', 'name')

    search = request.GET.get('search')
    if search:
        news = news.filter(name__icontains=search)

    paginator = Paginator(news, 8)
    page = int(request.GET.get('page', 1))
    news = paginator.get_page(page)

    return render(request, 'workspace/index.html', {'news': news})


def create_news(request):
    if request.method == 'POST':
        category_id = int(request.POST.get('category'))
        tag_ids = list(map(int, request.POST.getlist('tags')))
        tags = Tag.objects.filter(id__in=tag_ids)
        image = request.FILES.get('image')
        data = {
            'name': request.POST.get('name'),
            'description': request.POST.get('description'),
            'content': request.POST.get('content'),
            'is_published': request.POST.get('is_published', False) == 'on',
            'category': Category.objects.get(id=category_id)
        }

        news = News.objects.create(**data)
        news.tags.add(*tags)
        news.image.save(image.name, image)

        return redirect('/workspace/')

    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'workspace/create_news.html', {
        'categories': categories,
        'tags': tags,
    })

# Create your views here.
