from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet,TripDetailViewSet

router = DefaultRouter()
router.register(r'trips', TripViewSet)

router1=DefaultRouter()
router1.register(r'details', TripDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router1.urls)),
]