from django.urls import path, include
from session_app import views

urlpatterns = [
    path('set_session/',views.setsession),
    path('get_session/',views.getsession),
]
