from rest_framework import serializers
from .models import Registro_Pediatras, Generar_cita

class Registro_Pediatras_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Registro_Pediatras
        fields = '__all__'

class Generar_cita_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Generar_cita
        fields = '__all__'