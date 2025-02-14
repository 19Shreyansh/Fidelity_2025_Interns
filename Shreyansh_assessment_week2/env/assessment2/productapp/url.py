from django.urls import path,include
from productapp import views

urlpatterns = [
    path('postdata/',views.postdata,name='postdata'),
    path('getall/',views.getall,name='getall'),
    path('getbyid/<int:pk>/',views.getbyid,name='getbyid'),
    path('deleteid/<int:pk>/',views.deleteid,name='deleteid') ,
    path('update/<int:pk>/',views.update,name='update'),
]
