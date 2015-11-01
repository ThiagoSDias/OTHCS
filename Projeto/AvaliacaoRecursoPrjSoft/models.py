
from django.db import models

from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

ORIGEM_CHOICES = (
    (0, 'Interno'),
    (1, 'Externo'))

	
NIVEL_CHOICES = (
	 (0, 'Estagiario'),
	 (1, 'Junior'),
	 (2, 'Pleno'),
	 (3, 'Senior'))
	 
class Projeto(models.Model):
	nome_projeto = models.CharField(max_length=200)
	data_criacao = models.DateTimeField('date published')
	inicio_projeto = models.DateField()
	origem = models.IntegerField(choices=ORIGEM_CHOICES )
	nome_cliente = models.CharField(max_length=200)
	setor_emmpresa = models.CharField(max_length=200)
	
	def __str__(self):  # Python 2: def __unicode__(self):
		return self.nome_projeto	
	
class ConhecimentoNegocio(models.Model):
	projeto = models.ForeignKey(Projeto)
	nome_conhecimento_negocio = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nome_conhecimento_negocio		
	
class ConhecimentoTecnico(models.Model):
	projeto = models.ForeignKey(Projeto)
	nome_conhecimento_tecnico = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nome_conhecimento_tecnico	
	
		
class Especialidade(models.Model):
	especialidade = models.CharField(max_length=200)
	nivel = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
	
	def __str__(self):
		return self.especialidade	

class Funcionario(models.Model)	:
	matricula =  models.BigIntegerField()
	nome_funcionario = models.CharField(max_length=200)
	valor_hora = models.DecimalField( max_digits= 10, decimal_places=2)
	conhecimentos_tecnicos =  models.ManyToManyField(ConhecimentoTecnico, blank=True, null=True )
	conhecimentos_negocio =  models.ManyToManyField(ConhecimentoNegocio, blank=True, null=True)
	nivel =  models.IntegerField(choices=NIVEL_CHOICES)
	especialidades = models.ManyToManyField(Especialidade)
	projeto = models.ForeignKey(Projeto)
	
	def __str__(self):
		return u'%s %s' % (self.matricula, self.nome_funcionario)

class GrupoTarefa(models.Model)	:	
	nome_grupo	= models.CharField(max_length=200)
	complexidade  = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
	projeto = models.ForeignKey(Projeto)
	
	def __str__(self):
		return self.nome_grupo

class TipoTarefa(models.Model)	:	
	nome_tipo_tarefa = models.CharField(max_length=200)
	complexidade = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
	projeto = models.ForeignKey(Projeto)
	
	def __str__(self):
		return self.nome_tipo_tarefa
	
	
class Tarefa(models.Model)	 :
	nome_tarefa = models.CharField(max_length=200)
	Descricao_tarefa = models.CharField(max_length=200)
	data_previsao_inicio = models.DateField()
	tipo_tarefa = models.ForeignKey(TipoTarefa)
	grupo_tarefa = models.ForeignKey(GrupoTarefa)
	conhecimentos_tecnicos =  models.ManyToManyField(ConhecimentoTecnico, blank=True, null=True)
	conhecimentos_negocio =  models.ManyToManyField(ConhecimentoNegocio, blank=True, null=True)
	pontos_funcao_tarefa = models.DecimalField( max_digits= 10, decimal_places=2)
	projeto = models.ForeignKey(Projeto)
	
	def __str__(self):
		return u'%s %s' % (self.projeto, self.nome_tarefa)
		
class AlocacaoTarefa(models.Model)	 :
	tarefa = models.ForeignKey(Tarefa)
	especialidade = models.ForeignKey(Especialidade)
	recurso = models.ForeignKey(Funcionario)
	data_inicio = models.DateTimeField()
	data_previsao_termino = models.DateTimeField()
	data_conclusao = models.DateTimeField()
	complexidade_media = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
	horas_execucao_media = models.PositiveIntegerField()
	horas_estimada_ferramente = models.PositiveIntegerField()
	
	def __str__(self):
		return u'%s %s' % (self.tarefa, self.recurso)

		
class HistoricoTarefa(models.Model)	 :	
	tarefa = models.ForeignKey(Tarefa)
	especialidade = models.ForeignKey(Especialidade)
	recurso = models.ForeignKey(Funcionario)
	data_inicio = models.DateTimeField()
	data_conclusao = models.DateTimeField()
	porcentagem_conclusao = models.PositiveIntegerField(validators=[MaxValueValidator(100)]) 
	observacao = models.CharField(max_length=255) 
	repasse	= models.BooleanField()
	data_repasse = models.DateTimeField()
	
	def __str__(self):
		return u'%s %s' % (self.tarefa, self.recurso)
		
class PontuacaoTarefa(models.Model)	 :	
	tarefa = models.ForeignKey(Tarefa)
	especialidade = models.ForeignKey(Especialidade)	
	funcionario = models.ForeignKey(Funcionario)
	complexidade = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
	horas_execucao = models.PositiveIntegerField()	
	
	def __str__(self):
		return u'%s %s' % (self.tarefa, self.funcionario)