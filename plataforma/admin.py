from django.contrib import admin
from .models import Pacientes, DadosPaciente, Refeicao, Opcao

# Register your models here.
@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ("nome", "sexo", "idade")

@admin.register(DadosPaciente)
class DadosPacienteAdmin(admin.ModelAdmin):
    list_display = ("paciente",)

@admin.register(Refeicao)
class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ("paciente", "titulo")

@admin.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    list_display = ("refeicao",)