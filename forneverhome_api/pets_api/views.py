from django.shortcuts import render
from rest_framework import generics
from .serializers import PetsSerializer
from .models import Pets

# Create your views here.
class PetsList(generics.ListCreateAPIView):
    queryset = Pets.objects.all().order_by('id')
    serializer_class = PetsSerializer

class PetsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pets.objects.all().order_by('id')
    serializer_class = PetsSerializer
