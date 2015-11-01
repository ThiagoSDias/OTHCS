from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import Projeto, ConhecimentoNegocio, ConhecimentoTecnico, Especialidade
from .models import Funcionario, GrupoTarefa, TipoTarefa, Tarefa, AlocacaoTarefa, HistoricoTarefa, PontuacaoTarefa

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome_projeto', 'data_criacao', 'inicio_projeto' )
    search_fields = ('nome_projeto', 'nome_cliente')

class ConhecimentoNegocioAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'nome_conhecimento_negocio' )
    search_fields = ('projeto', 'nome_conhecimento_negocio' )

class ConhecimentoTecnicoAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'nome_conhecimento_tecnico' )
    search_fields = ('projeto', 'nome_conhecimento_tecnico' )

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('especialidade', 'nivel' )
    search_fields = ('especialidade', 'nivel' )

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome_funcionario', 'valor_hora', 'nivel' )
    search_fields = ('matricula', 'nome_funcionario', 'valor_hora', 'nivel')
    formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple},}

class GrupoTarefaAdmin(admin.ModelAdmin):
    list_display = ('nome_grupo', 'complexidade', 'projeto')
    search_fields = ('nome_grupo', 'complexidade', 'projeto')

class TipoTarefaAdmin(admin.ModelAdmin):
    list_display = ('nome_tipo_tarefa', 'complexidade', 'projeto')
    search_fields = ('nome_tipo_tarefa', 'complexidade', 'projeto')

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome_tarefa', 'Descricao_tarefa', 'data_previsao_inicio','tipo_tarefa', 'grupo_tarefa', 'projeto')
    search_fields = ('nome_tarefa', 'Descricao_tarefa','tipo_tarefa', 'grupo_tarefa', 'projeto')
    formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple},}

class AlocacaoTarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'especialidade', 'recurso', 'data_inicio', 'data_conclusao', 'complexidade_media')
    search_fields = ('tarefa', 'especialidade', 'recurso')

class HistoricoTarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'especialidade', 'recurso', 'data_inicio', 'data_conclusao', 'repasse')
    search_fields = ('tarefa', 'especialidade', 'recurso')

class PontuacaoTarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'especialidade', 'funcionario', 'complexidade', 'horas_execucao')
    search_fields = ('tarefa', 'especialidade', 'funcionario')	


	
admin.site.register(Projeto,ProjetoAdmin)
admin.site.register(ConhecimentoNegocio, ConhecimentoNegocioAdmin)
admin.site.register(ConhecimentoTecnico, ConhecimentoTecnicoAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(GrupoTarefa, GrupoTarefaAdmin)
admin.site.register(TipoTarefa, TipoTarefaAdmin)
admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(AlocacaoTarefa, AlocacaoTarefaAdmin)
admin.site.register(HistoricoTarefa, HistoricoTarefaAdmin)
admin.site.register(PontuacaoTarefa, PontuacaoTarefaAdmin)