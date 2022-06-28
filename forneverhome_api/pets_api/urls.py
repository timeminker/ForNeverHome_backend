from django.urls import path
from . import views

urlpatterns = [
    path('api/pets', views.PetsList.as_view(), name='pets_list'),
    path('api/pets/<int:pk>', views.PetsDetail.as_view(), name='pets_detail'), 
]
