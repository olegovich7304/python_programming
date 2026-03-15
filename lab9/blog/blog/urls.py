from django.contrib import admin
from django.urls import path
from articles import views
from articles.views import get_article
from articles.views import input_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('archive/', views.archive),
    path('article/<int:article_id>/', get_article, name='get_article'),
    path('article/new/', views.create_post, name='create_post'),
    path('registration/', views.create_user, name='registration'),
    path('auth/', input_user, name='auth'),    
]
