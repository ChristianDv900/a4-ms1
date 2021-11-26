from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.contrib.auth.models import User

# Create your models here.

class paciente(models.Model):
   
    edad     = models.IntegerField(null=True)
    # user      =models.ForeignKey(User,  on_delete=models.CASCADE)
    user      =models.OneToOneField(User,  on_delete=models.CASCADE)
class medico(models.Model):
  
    edad     = models.IntegerField(null=True)
    especialidad =models.CharField(max_length=64, default="General")  
    #user      =models.ForeignKey(User,  on_delete=models.CASCADE)
    user      =models.OneToOneField(User,  on_delete=models.CASCADE)