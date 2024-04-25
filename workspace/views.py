from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from news.models import News
# from django.contrib.auth.decorators import login_required
from workspace.decorators import login_required, own_news
from workspace.forms import NewsForm, LoginForm


@login_required(login_url='/auth/login/')
def workspace(request):

    news = News.objects.filter(author=request.user).order_by('-date', 'name')
    search = request.GET.get('search')
    if search:
        news = news.filter(name__icontains=search)

    paginator = Paginator(news, 8)
    page = int(request.GET.get('page', 1))
    news = paginator.get_page(page)

    return render(request, 'workspace/index.html', {'news': news})


# def create_news(request):
#     if request.method == 'POST':
#         category_id = int(request.POST.get('category'))
#         tag_ids = list(map(int, request.POST.getlist('tags')))
#         tags = Tag.objects.filter(id__in=tag_ids)
#         image = request.FILES.get('image')
#         data = {
#             'name': request.POST.get('name'),
#             'description': request.POST.get('description'),
#             'content': request.POST.get('content'),
#             'is_published': request.POST.get('is_published', False) == 'on',
#             'category': Category.objects.get(id=category_id)
#         }
#
#         news = News.objects.create(**data)
#         news.tags.add(*tags)
#         news.image.save(image.name, image)
#
#         return redirect('/workspace/')
#
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     return render(request, 'workspace/create_news.html', {
#         'categories': categories,
#         'tags': tags,
#     })


@login_required()
def create_news(request):

    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            messages.success(request, f'The news "{news.name}" has been successfully created!')

            return redirect('/workspace/')

        messages.error(request, f'Correct errors below')

    return render(request, 'workspace/create_news.html', {'form': form})


# def update_news(request, id):
#     news = get_object_or_404(News, id=id)
#
#     if request.method == 'POST':
#         category_id = int(request.POST.get('category'))
#         tag_ids = list(map(int, request.POST.getlist('tags')))
#         tags = Tag.objects.filter(id__in=tag_ids)
#         image = request.FILES.get('image')
#
#         if image:
#             news.image.save(image.name, image)
#
#         news.tags.clear()
#         news.tags.add(*tags)
#
#         news.name = request.POST.get('name')
#         news.description = request.POST.get('description')
#         news.content = request.POST.get('content')
#         news.is_published = request.POST.get('is_published', False) == 'on'
#         news.category = Category.objects.get(id=category_id)
#         news.save()
#
#         return redirect('/workspace/')
#
#     tags = Tag.objects.all()
#     categories = Category.objects.all()
#     return render(request, 'workspace/update_news.html', {
#         'news': news,
#         'categories': categories,
#         'tags': tags,
#     })


@login_required()
@own_news
def update_news(request, id):

    news = get_object_or_404(News, id=id)
    form = NewsForm(instance=news)

    if request.method == 'POST':
        form = NewsForm(instance=news, files=request.FILES, data=request.POST)
        if form.is_valid():
            news = form.save()
            messages.success(request, f'The news "{news.name}" has been successfully updated!')
            return redirect('/workspace/')
        messages.error(request, f'Correct errors below')

    return render(request, 'workspace/update_news.html', {
        'news': news,
        'form': form
    })


@login_required()
@own_news
def delete_news(request, id):

    news = get_object_or_404(News, id=id)
    name = news.name
    news.delete()
    messages.success(request, f'The news "{name}" has been successfully deleted!')
    return redirect('/workspace/')


def login_profile(request):

    form = LoginForm()
    message = None

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, f'Welcome to workspace "{user.first_name} {user.last_name}"')
                return redirect('/workspace/')

            message = 'The user does not exist or the password is incorrect.'

    return render(request, 'auth/login.html', {'form': form, 'message': message})


def logout_profile(request):

    if request.user.is_authenticated:
        logout(request)

    return redirect('/')

# Create your views here.
