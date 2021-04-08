from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/', include('diary.urls')),
    path('blog/', include('blog.urls')),
    path('bbs/', include('bbs.urls')),
    path('', include('page.urls')),
]

handler404 = 'page.views.page_not_found'
handler404 = 'page.views.server_error'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)