from django.db import models
from django.utils import timezone


class CategoriaTurmaModel(models.Model):
    categoria_turma_nome = models.CharField(max_length=100, blank=True)


class TurmaModel(models.Model):
    turma_nome = models.CharField(max_length=100, blank=True)
    turma_categoria_nome = models.ForeignKey(CategoriaTurmaModel, on_delete=models.DO_NOTHING)  # noqa:E501


class TaxonomiaModel(models.Model):
    taxonomia_nome = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.taxonomia_nome


class DisciplinaModel(models.Model):
    disciplina_nome = models.CharField(max_length=100, blank=True)


class PlanejamentoSemanalModel(models.Model):
    planejamento_semanal_criador = models.EmailField(blank=True)
    planejamento_semanal_turma = models.CharField(max_length=255, blank=True)  # noqa:E501
    planejamento_semanal_disciplina = models.CharField(max_length=255, blank=True)  # noqa:E501
    planejamento_semanal_taxonomia = models.CharField(max_length=255, blank=True)  # noqa:E501
    planejamento_semanal_hora_aula = models.CharField(max_length=255, blank=True)
    planejamento_semanal_dt_inicio = models.DateField(blank=True)
    planejamento_semanal_descricao = models.TextField(blank=True)
    registro_planejamento_semanal_dt = models.DateField(default=timezone.now, blank=True)


class RegistroPlanejamentoSemanalModel(models.Model):
    registro_planejamento_semanal = models.TextField(blank=True)  # noqa:E501
    registro_planejamento_semanal_dt = models.DateField(default=timezone.now, blank=True)  # noqa:E501
