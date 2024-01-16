from django import forms
from django_summernote.widgets import SummernoteWidget

from app.models import PlanejamentoSemanalModel


class PlanejamentoSemanalForm(forms.ModelForm):
    """
    planejamento_semanal_criador = models.EmailField(blank=True)
    planejamento_semanal_turma = models.CharField(max_length=255, blank=True)  # noqa:E501
    planejamento_semanal_disciplina = models.CharField(max_length=255, blank=True)  # noqa:E501
    planejamento_semanal_taxonomia = models.CharField(max_length=255, blank=True)  # noqa:E501
    planejamento_semanal_hora_aula = models.CharField(max_length=255, blank=True)
    planejamento_semanal_dt_inicio = models.DateField(blank=True)
    planejamento_semanal_descricao = models.TextField(blank=True)
    registro_planejamento_semanal_dt = models.DateField(default=timezone.now, blank=True)
    """
    planejamento_semanal_descricao = forms.CharField(
        widget=SummernoteWidget()
    )

    class Meta:
        model = PlanejamentoSemanalModel
        fields = (
            'planejamento_semanal_criador',
            'planejamento_semanal_turma',
            'planejamento_semanal_disciplina',
            'planejamento_semanal_taxonomia',
            'planejamento_semanal_hora_aula',
            'planejamento_semanal_dt_inicio',
            'planejamento_semanal_descricao'
        )
        widgets = {
            'planejamento_semanal_turma': forms.SelectMultiple(
                attrs={
                    'class': 'form-select',
                    'aria-label': 'multiple select example'
                }
            ),
            'planejamento_semanal_disciplina': forms.SelectMultiple(
                attrs={
                    'class': 'form-select',
                    'aria-label': 'multiple select example'
                }
            ),
            'planejamento_semanal_taxonomia': forms.SelectMultiple(
                attrs={
                    'class': 'form-select',
                    'aria-label': 'multiple select example'
                }
            ),
            'planejamento_semanal_hora_aula': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'planejamento_semanal_dt_inicio': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'planejamento_semanal_criador': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
