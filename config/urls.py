from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    # path('about/', include('about.urls')),
    # path('pages/', include('pages.urls')),
    # path('services/', include('services.urls')),
    # path('membership/', include('membership.urls')),
    path('blog/', include('blog.urls')),
    # path('contact/', include('contact.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)