import requests
from django.shortcuts import render, redirect, HttpResponse
from app.models import Turma, Serie, Disciplina


# Usuário para autenticação na api do sophia
ACESSO_SOPHIA = {"usuario": "setape", "senha": "setape"}

# Endpoints
POST_AUTH = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Autenticacao"  # noqa: E501
GET_STUDENTS = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Alunos"
GET_STUDENT = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Alunos/"
PUT_STUDENTS = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Alunos/"
GET_CLASSROOM = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Turmas"
GET_DISCIPLINA = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Disciplinas"  # noqa: E501


# Conectando com a api do sophia
def conecta_com_sophia():
    acesso = {
        'token': requests.post(POST_AUTH, json=ACESSO_SOPHIA).text
    }
    return acesso


def armazenar_turmas_db(request, ):
    obj_turmas = []
    teste_2 = requests.get(GET_CLASSROOM, headers=conecta_com_sophia()).json()

    for i in teste_2:
        if i['periodoLetivo']['descricao'] in ['.Ano 2024', '.Sem2024.1']:
            for c in i['professoresDisciplinas']:
                obj_turmas.append(
                    {'turma': '', 'nome': i['nome'],
                     'disciplina': c['disciplina']['nome']}
                )
                if 'Téc' in i['nome']:
                    try:
                        Turma.objects.create(
                            nome_turma=i['nome'],
                            serie=Serie.objects.get(
                                nome_serie='Ensino Técnico')
                        )

                    except Exception:
                        pass
                    Disciplina.objects.create(
                        nome_disciplina=c['disciplina']['nome'],
                        serie=Serie.objects.get(
                            nome_serie='Ensino Técnico')
                    )
                elif 'EM' in i['nome'] or '9º' in i['nome']:
                    if 'Programa' in i['nome'] or 'Preparatório' in i['nome']:
                        pass
                    else:
                        try:
                            Turma.objects.create(
                                nome_turma=i['nome'],
                                serie=Serie.objects.get(
                                    nome_serie='Ensino Médio')
                            )

                        except Exception:
                            pass
                        Disciplina.objects.create(
                            nome_disciplina=c['disciplina']['nome'],
                            serie=Serie.objects.get(
                                nome_serie='Ensino Médio')
                        )
                elif 'Jardim' in i['nome'] or 'Maternal' in i['nome']:
                    try:
                        Turma.objects.create(
                            nome_turma=i['nome'],
                            serie=Serie.objects.get(
                                nome_serie='Ensino Infantil')
                        )

                    except Exception:
                        pass
                    Disciplina.objects.create(
                        nome_disciplina=c['disciplina']['nome'],
                        serie=Serie.objects.get(
                            nome_serie='Ensino Infantil')
                    )
                elif 'º' in i['nome']:
                    if 'PEC' in i['nome']:
                        ...
                    else:
                        try:
                            Turma.objects.create(
                                nome_turma=i['nome'],
                                serie=Serie.objects.get(
                                    nome_serie='Ensino Fundamental')
                            )

                        except Exception:
                            pass
                        Disciplina.objects.create(
                            nome_disciplina=c['disciplina']['nome'],
                            serie=Serie.objects.get(
                                nome_serie='Ensino Fundamental')
                        )
                else:
                    if 'ADS' in i['nome'] or 'PSI' in i['nome'] or 'DIR' in i['nome'] or 'PED' in i['nome'] or 'ENF' in i['nome']:
                        try:
                            Turma.objects.create(
                                nome_turma=i['nome'],
                                serie=Serie.objects.get(
                                    nome_serie='Ensino Superior')
                            )
                        except Exception:
                            pass
                        Disciplina.objects.create(
                            nome_disciplina=c['disciplina']['nome'],
                            serie=Serie.objects.get(
                                nome_serie='Ensino Superior')
                        )

    return HttpResponse(Turma.objects.all())
