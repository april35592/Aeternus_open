from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.CategoryList.as_view(), name='category'),
    path('<str:slug>/', views.postList, name='postList'),
    path('<str:slug>/<int:pk>/', views.PostDetail.as_view(), name='postDetail'),
]
