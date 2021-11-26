from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import paciente, medico
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['username', 'email']

class PacienteSerilizer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = paciente
        fields =['user','edad']

class MedicoSerilizer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = medico
        fields =['user','especialidad','edad']