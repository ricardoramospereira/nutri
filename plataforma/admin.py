from django.contrib import admin
from .models import Pacientes, DadosPaciente

# Register your models here.
@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ("nome", "sexo", "idade")

@admin.register(DadosPaciente)
class DadosPacienteAdmin(admin.ModelAdmin):
    list_display = ("paciente",)