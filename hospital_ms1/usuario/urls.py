from django.urls import path
from .views import PacienteListCreate,PacienteUpdateDelete,MedicoListCreate,MedicoUpdateDelete
urlpatterns =[
    path('pacientes/', PacienteListCreate.as_view()),
    path('pacientes/<pk>', PacienteUpdateDelete.as_view()),
    path('medicos/',MedicoListCreate.as_view()),
    path('medicos/<pk>/',MedicoUpdateDelete.as_view()),
] 