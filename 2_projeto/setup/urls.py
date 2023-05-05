from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('blog.urls')),
    path('post/<int:post_id>', views.post),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
