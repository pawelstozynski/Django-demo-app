from django.urls import path

from .views import article_views, error_views, pages_views, todo_views

urlpatterns = [
    path('404/', error_views.error_404, name='error-404'),
    path('500/', error_views.error_500, name='error-500'),
    path('', pages_views.home, name='home'),
    path('article/', article_views.article_list, name='article-list'),
    path('article/search/', article_views.article_search, name='article-search'),
    path('article/<int:article_id>/', article_views.article_show, name='article-show'),
    path('article/create/', article_views.article_create, name='article-create'),
    path('article/<int:article_id>/edit/', article_views.article_edit, name='article-edit'),
    path('article/<int:article_id>/delete/', article_views.article_delete, name='article-delete'),
    path('todo/', todo_views.todo_list, name='todo-list'),
    path('todo/create/', todo_views.todo_create, name='todo-create'),
    path('todo/<int:todo_id>/delete/', todo_views.todo_delete, name='todo-delete'),
]