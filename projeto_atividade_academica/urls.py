
from django.contrib import admin
from django.urls import path, include
from django.conf import settings           #para visualizar aenxos
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
        path('accounts/', include('usuarios.urls', namespace='usuarios')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)