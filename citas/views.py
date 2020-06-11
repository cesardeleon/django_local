from django.shortcuts import render
from rest_framework import viewsets
from .models import Registro_Pediatras, Generar_cita
from .serializers import Registro_Pediatras_Serializer, Generar_cita_Serializer
# Create your views here.

class Registro_Pediatras_View_Set(viewsets.ModelViewSet):
    serializer_class = Registro_Pediatras_Serializer
    queryset = Registro_Pediatras.objects.all()

class Generar_cita_View_Set(viewsets.ModelViewSet):
    serializer_class = Generar_cita_Serializer
    queryset = Generar_cita.objects.all()
    