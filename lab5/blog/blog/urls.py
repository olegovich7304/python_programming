from django.contrib import admin
from django.urls import path
from articles import views
from articles.views import get_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('archive/', views.archive),
    path('article/<int:article_id>/', get_article, name='get_article'),
    path('article/new/', views.create_post, name='create_post'),
]
