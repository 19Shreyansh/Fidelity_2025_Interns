
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name='home'),
    path('showpro/',views.showpro,name='show'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('update/<str:eID>',views.update,name='update'),
    path('delete/<str:eID>/', views.delete, name='delete'),
]
