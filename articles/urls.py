from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment', views.leave_comment, name='leave_comment'),
    path('create_article/', views.create_article, name='create_article'),
    path('create/', views.create, name='create'),
]
