from django.urls import path, include
from cbv_app.views import Myclass,index
from cbv_app.views import CreateProd,UpdateProd,DeleteProd

urlpatterns = [
    path('cbvhome/',Myclass.as_view,name='cbv_home'),
    path('create/',CreateProd.as_view(),name='create_product'),
    path('show/',index,name='show'),
    path('update/<int:pk>',UpdateProd.as_view(),name='update_product'),
    path('delete/<int:pk>',DeleteProd.as_view(),name='delete_product'),
    # path('get/',views.getsession),
]