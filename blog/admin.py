from django.contrib import admin
from .models import Category, Post, Image

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Image)