from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.diary, name='main'),
    path('upload_image/', views.uploadImage, name='upload_image'),
    path('delete_image/<int:image_id>/', views.deleteImage, name='delete_image'),
    path('create_reply/<int:image_id>/', views.createReply, name='create_reply'),
    path('delete_reply/<int:reply_id>/', views.deleteReply, name='delete_reply')
]
