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
        turmas = []
        disciplinas = []
        
        id_serie = Serie.objects.get(nome_serie=turma)

        for turma in Turma.objects.filter(serie=turma):
            turmas.append(turma.nome_turma)

        for disciplina in Disciplina.objects.filter(serie=id_serie.nome_serie):
            disciplinas.append(disciplina.nome_disciplina)

        if request.method == 'POST':
            print(request.POST.get)
            body = {
                'plano_1': [
                    request.POST.get('turmas1', ''),
                    request.POST.get('disciplinas1', ''),
                    request.POST.get('date_i1', ''),
                    request.POST.get('date_f1', ''),
                    request.POST.get('plano1', ''),
                ],
                'plano_2': [
                    request.POST.get('turmas2', ''),
                    request.POST.get('disciplinas2', ''),
                    request.POST.get('date_i2', ''),
                    request.POST.get('date_f2', ''),
                    request.POST.get('plano2', ''),
                ],
                'plano_3': [
                    request.POST.get('turmas3', ''),
                    request.POST.get('disciplinas3', ''),
                    request.POST.get('date_i3', ''),
                    request.POST.get('date_f3', ''),
                    request.POST.get('plano3', ''),
                ],
                'plano_4': [
                    request.POST.get('turmas4', ''),
                    request.POST.get('disciplinas4', ''),
                    request.POST.get('date_i4', ''),
                    request.POST.get('date_f4', ''),
                    request.POST.get('plano4', ''),
                ],
                'plano_5': [
                    request.POST.get('turmas5', ''),
                    request.POST.get('disciplinas5', ''),
                    request.POST.get('date_i5', ''),
                    request.POST.get('date_f5', ''),
                    request.POST.get('plano5', ''),
                ],
            }
            print(body)
            return redirect(
                'accounts:escolher_curso_para_planejamento_semanal',
            )
        else:

            return render(
                request,
                'planejamento_semanal/planejamento_semanal.html',
                {'turmas': turmas, 'disciplinas': disciplinas}
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
                'registros': PlanejamentoSemanal.objects.filter(
                    planejamento_semanal_criador=request.user.email
                )
            }
        )
    else:
        return redirect('accounts:home')
