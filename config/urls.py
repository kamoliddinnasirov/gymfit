from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('services/', include('services.urls')),
    path('contact/', include('contact.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
