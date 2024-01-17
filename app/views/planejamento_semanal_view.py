from django.shortcuts import redirect, render
from app.models import Serie, PlanejamentoSemanal, Turma, Taxonomia, Disciplina  # noqa: F403 E501


# O usuário deve escolher qual série ele deseja iniciar um planjemaneto.
# Ao selecionar o usuário é redirecionado para a página do formulário
# de planejamento de ensino.
def escolher_curso_para_planejamento_semanal(request, username) -> render:
    # Verifica se o usuário está autenticado.
    if request.user.is_authenticated:
        # Dados das séries.
        series = Serie.objects.all()

        # Se o método da socilitação for post.
        # Deve retornar para a página do formulário junto com a info
        # de qual turma pegar as disciplinas
        if request.method == 'POST':
            # É necessário passar o usuario e o dado da turma
            return redirect('accounts:planejamento_semanal', request.user.username, request.POST.get('turma'))  # noqa: E501
        # Retorna o template para escolher a turma
        return render(
            request,
            'planejamento_semanal/escolher_curso_para_planejamento_semanal.html',  # noqa: E501
            {'series': series}
        )
    else:
        return redirect('accounts:home')


def planejamento_semanal(request, username, turma):
    if request.user.is_authenticated:
        turmas = [t.nome_turma for t in Turma.objects.filter(serie=turma)]
        disciplinas = [
            d.nome_disciplina for d in Disciplina.objects.filter(serie=turma)]
        taxonomia = [tx.nome_taxonomia for tx in Taxonomia.objects.all()]

        if request.method == 'POST':
            print(request.POST.get('turmas1', ''))
            if request.POST.get('turmas1'):
                PlanejamentoSemanal.objects.create(
                    planejamento_semanal_criador=request.user.email,
                    planejamento_semanal_turma=request.POST.get('turmas1', ''),
                    planejamento_semanal_disciplina=request.POST.get(
                        'disciplina1', ''),
                    planejamento_semanal_taxonomia=request.POST.get(
                        'taxonomia1', ''),
                    planejamento_semanal_hora_aula=request.POST.get(
                        'hora_aula1', ''),
                    planejamento_semanal_dt_inicio=request.POST.get(
                        'date_i1', ''),
                    planejamento_semanal_dt_final=request.POST.get(
                        'date_f1', ''),
                    planejamento_semanal_descricao=request.POST.get(
                        'descricao1')
                )
            elif request.POST.get('turmas2', ''):
                PlanejamentoSemanal.objects.create(
                    planejamento_semanal_criador=request.user.email,
                    planejamento_semanal_turma=request.POST.get('turmas2', ''),
                    planejamento_semanal_disciplina=request.POST.get(
                        'disciplina2', ''),
                    planejamento_semanal_taxonomia=request.POST.get(
                        'taxonomia2', ''),
                    planejamento_semanal_hora_aula=request.POST.get(
                        'hora_aula2', ''),
                    planejamento_semanal_dt_inicio=request.POST.get(
                        'date_i2', ''),
                    planejamento_semanal_dt_final=request.POST.get(
                        'date_f2', ''),
                    planejamento_semanal_descricao=request.POST.get(
                        'descricao2')
                )
            elif request.POST.get('turmas3', ''):
                PlanejamentoSemanal.objects.create(
                    planejamento_semanal_criador=request.user.email,
                    planejamento_semanal_turma=request.POST.get('turmas3', ''),
                    planejamento_semanal_disciplina=request.POST.get(
                        'disciplina3', ''),
                    planejamento_semanal_taxonomia=request.POST.get(
                        'taxonomia3', ''),
                    planejamento_semanal_hora_aula=request.POST.get(
                        'hora_aula3', ''),
                    planejamento_semanal_dt_inicio=request.POST.get(
                        'date_i3', ''),
                    planejamento_semanal_dt_final=request.POST.get(
                        'date_f3', ''),
                    planejamento_semanal_descricao=request.POST.get(
                        'descricao3')
                )
            elif request.POST.get('turmas4', ''):
                PlanejamentoSemanal.objects.create(
                    planejamento_semanal_criador=request.user.email,
                    planejamento_semanal_turma=request.POST.get('turmas4', ''),
                    planejamento_semanal_disciplina=request.POST.get(
                        'disciplina4', ''),
                    planejamento_semanal_taxonomia=request.POST.get(
                        'taxonomia4', ''),
                    planejamento_semanal_hora_aula=request.POST.get(
                        'hora_aula4', ''),
                    planejamento_semanal_dt_inicio=request.POST.get(
                        'date_i4', ''),
                    planejamento_semanal_dt_final=request.POST.get(
                        'date_f4', ''),
                    planejamento_semanal_descricao=request.POST.get(
                        'descricao4')
                )
            elif request.POST.get('turmas5', ''):
                PlanejamentoSemanal.objects.create(
                    planejamento_semanal_criador=request.user.email,
                    planejamento_semanal_turma=request.POST.get('turmas5', ''),
                    planejamento_semanal_disciplina=request.POST.get(
                        'disciplina5', ''),
                    planejamento_semanal_taxonomia=request.POST.get(
                        'taxonomia5', ''),
                    planejamento_semanal_hora_aula=request.POST.get(
                        'hora_aula5', ''),
                    planejamento_semanal_dt_inicio=request.POST.get(
                        'date_i5', ''),
                    planejamento_semanal_dt_final=request.POST.get(
                        'date_f5', ''),
                    planejamento_semanal_descricao=request.POST.get(
                        'descricao5')
                )

            return redirect(
                'accounts:escolher_curso_para_planejamento_semanal', request.user.username
            )
        else:

            return render(
                request,
                'planejamento_semanal/planejamento_semanal.html',
                {'turmas': turmas, 'disciplinas': disciplinas,
                    'taxonomias': taxonomia}
            )
    else:
        return redirect('accounts:home')


def meus_planejamentos(request, username):
    if request.user.is_authenticated:
        # Se o usuário estiver corretamente autenticado
        # retorna o template que contém os planejamentos
        # que contém seu email como criador
        return render(
            request,
            'planejamento_semanal/meus_planejamentos.html',
            {
                'registros': PlanejamentoSemanal.objects.all()
            }
        )
    else:
        return redirect('accounts:home')


def ver_planejamento(request, username, id_planejamento):
    planejamento = PlanejamentoSemanal.objects.get(id=id_planejamento)
    return render(request, 'planejamento_semanal/ver_planejamento.html', {'planejamento': planejamento})
