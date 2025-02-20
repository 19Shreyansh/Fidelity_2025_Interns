from django.urls import path,include
from restapp import views
from drf_yasg.views import get_schema_view
# from rest_framework.schemas import get_schema_view
from drf_yasg import openapi


#queryset = collection of objects coming from the database

schema_view = get_schema_view(openapi.Info(title="Student API",default_version='1.2',
                                           description="std version",terms_of_service="",
                                           contact=openapi.Contact(email="shreyanshsri23@gmail.com"),
                                                                   license=openapi.License("Open")),public=True)

urlpatterns = [
    path('postdata/',views.postdata,name='postdata'),
    path('getall/',views.getall,name='getall'),
    path('getbyid/<int:pk>/',views.getbyid,name='getbyid'),
    path('deleteid/<int:pk>/',views.deleteid,name='deleteid') ,
    path('update/<int:pk>/',views.update,name='update'),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0)),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0)),  
]
