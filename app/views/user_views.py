from django.shortcuts import render, redirect
from app.utils import classroom_of_sophia, subjects_of_sophia
from ..models import TaxonomiaModel, PlanejamentoSemanalModel


def user_dashboard_home(request,):
    if request.user.is_authenticated:
        return render(request, 'pages/index.html', {'context': 'context'})
    else:
        return redirect('/')


def user_planejamento_semanal(request, ):
    if request.user.is_authenticated:
        if request.method == 'POST':
            formulario = PlanejamentoSemanalModel(
                planejamento_semanal_criador=request.user,  # noqa: E501
                planejamento_semanal_turma=request.POST.get('turmas'),  # noqa: E501
                planejamento_semanal_disciplina=request.POST.get('disciplinas'),  # noqa: E501
                planejamento_semanal_taxonomia=request.POST.get('taxonomias'),  # noqa: E501
                planejamento_semanal_hora_aula=request.POST.get('hora_aula'),  # noqa: E501
                planejamento_semanal_dt_inicio=request.POST.get('data'),  # noqa: E501
                planejamento_semanal_descricao=request.POST.get('descricao')  # noqa: E501
            )

            formulario.save()

            return render(
                request, 'pages/planejamento_semanal.html', {
                    'turmas': [turma['nome'] for turma in classroom_of_sophia()],  # noqa: E501
                    'disciplinas': [disciplina['nome'] for disciplina in subjects_of_sophia()],  # noqa: E501
                    'taxonomias': TaxonomiaModel.objects.all().order_by('-id'),  # noqa: E501
                    'registros': PlanejamentoSemanalModel.objects.all().order_by('-id')  # noqa: E501
                }
            )
        else:
            return render(
                request, 'pages/planejamento_semanal.html', {
                    'turmas': [turma['nome'] for turma in classroom_of_sophia()],  # noqa: E501
                    'disciplinas': [disciplina['nome'] for disciplina in subjects_of_sophia()],  # noqa: E501
                    'taxonomias': TaxonomiaModel.objects.all().order_by('-id'),  # noqa: E501
                    'registros': PlanejamentoSemanalModel.objects.all().order_by('-id')  # noqa: E501
                }
            )
    else:
        return redirect('/')
