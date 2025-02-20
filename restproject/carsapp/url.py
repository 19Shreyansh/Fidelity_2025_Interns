from django.urls import path,include
from .views import CarListView,CarDetailView,CarDeleteView,CarCreateView,CarUpdateView

urlpatterns = [
    path('list/',CarListView.as_view(),name='cars_list'),
    path('create/',CarCreateView.as_view(),name='cars_create'),
    path('cars/<int:pk>/',CarDetailView.as_view(),name='car_detail'),
    path('update/<int:pk>/',CarUpdateView.as_view(),name='car_update'),
    path('delete/<int:pk>/',CarDeleteView.as_view(),name='car_delete'),
]