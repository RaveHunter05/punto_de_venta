from django.contrib import admin
from django.urls import path

from posts.views import post_list_view
from principal.views import principal

# Esto es para las imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', post_list_view),
    path('', principal)
]

#Esto también es para la configuración de la ruta de las imágenes

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
