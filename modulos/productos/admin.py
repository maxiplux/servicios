from django.contrib import admin

# Register your models here.
from .models import clases
from modulos.utilidades.utiladmin import GenerateAdmins




GenerateAdmins(clases())