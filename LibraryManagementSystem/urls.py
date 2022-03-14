from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import send_gmail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
    path('send_gmail/',send_gmail,name="send_gmail"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'library.views.error_500'
