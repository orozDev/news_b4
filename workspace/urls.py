from django.urls import path
from . import views


urlpatterns = [
    path('', views.workspace, name='workspace'),
    path('news/', views.workspace),
    path('news/create/', views.create_news, name='create_news'),
]