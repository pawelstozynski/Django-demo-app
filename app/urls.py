from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.article_show, name='article-show'),
    path('article/create/', views.article_create, name='article-create'),
    path('article/<int:article_id>/edit/', views.article_edit, name='article-edit'),
    path('article/<int:article_id>/delete/', views.article_delete, name='article-delete'),
]