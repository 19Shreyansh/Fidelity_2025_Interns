from rest_framework import routers
from .views import QuestionViewSet
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

route=routers.DefaultRouter()

route.register('question',QuestionViewSet,basename='QUESTION')

schema_view = get_schema_view(openapi.Info(title="Question_Paper_API",default_version='1.0.0',
                                           description="Questions",terms_of_service="",
                                           contact=openapi.Contact(email="shreyanshsri23@gmail.com"),
                                                                   license=openapi.License("Open")),public=True)

urlpatterns=[
    path('paper/',include(route.urls)),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0)),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0)),   
]

