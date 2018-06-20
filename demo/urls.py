from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

from app.views import error_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

handler404 = error_views.error_404
handler500 = error_views.error_500