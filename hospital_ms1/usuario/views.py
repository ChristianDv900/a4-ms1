from django.shortcuts import render
from rest_framework import generics
from .serializers import PacienteSerilizer,MedicoSerilizer
from .models import paciente,medico
# Create your views here.


class PacienteListCreate(generics.ListCreateAPIView):
    queryset = paciente.objects.all()
    serializer_class =PacienteSerilizer

class PacienteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    querySet =paciente.objects.all()
    serializer_class =PacienteSerilizer

class MedicoListCreate(generics.ListCreateAPIView):
    queryset = medico.objects.all()
    serializer_class =MedicoSerilizer

class MedicoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    querySet =medico.objects.all()
    serializer_class =MedicoSerilizer
