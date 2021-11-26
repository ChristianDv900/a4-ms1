from django.contrib import admin
from .models import paciente, medico

# Register your models here.

admin.site.register(paciente)
admin.site.register(medico)