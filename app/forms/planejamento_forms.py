from django import forms
from app.models import PlanejamentoSemanal


class PlanejamentoSemanalForm(forms.ModelForm):

    class Meta:
        model = PlanejamentoSemanal
        fields = '__all__'
        exclude = (
            'planejamento_semanal_criador',
            'registro_planejamento_semanal_dt'
        )
        widgets = {
            'planejamento_semanal_dt_inicio': forms.DateInput(
                attrs={
                    'type': 'date',
                },
            ),
            'planejamento_semanal_dt_final': forms.DateInput(
                attrs={
                    'type': 'date',
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            print(field.widget)
            field.widget.attrs['class'] = 'form-control mb-3'
