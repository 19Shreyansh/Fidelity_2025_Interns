from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restapp/', include('restapp.url')),
    path('carsapp/', include('carsapp.url')),
]
