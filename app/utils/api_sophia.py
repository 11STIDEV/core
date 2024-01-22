import requests
from app.models import Serie, PlanejamentoSemanal

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


# Recursos da API
# Turmas
def recurso_turma():
    turmas = [
        x['nome'] for x in requests.get(
            GET_CLASSROOM,
            headers=conecta_com_sophia()).json() if x['curso']['tipoCurso'] == 'Curso Curricular'  # noqa: E501
    ]

    return turmas


# Disciplinas
def recurso_disciplina():
    return requests.get(GET_DISCIPLINA, headers=conecta_com_sophia()).json()


def teste():
    return requests.get(GET_CLASSROOM, headers=conecta_com_sophia()).json()


def turmas_disciplinas():
    obj_turmas = []
    teste_2 = teste()

    for i in teste_2:
        if 'Téc' in i['nome']:
            turma = ('Ensino Técnico')
        elif 'EM' in i['nome'] or '9º' in i['nome']:
            if 'Programa' in i['nome'] or 'Preparatório' in i['nome']:
                pass
            else:
                turma = ('Ensino Médio')
        elif 'Jardim' in i['nome'] or 'Maternal' in i['nome']:
            turma = ('Ensino Infantil')
        elif 'º' in i['nome']:
            if 'PEC' in i['nome']:
                ...
            else:
                turma = ('Ensino Fundamental')
        else:
            if 'ADS' in i['nome'] or 'PSI' in i['nome'] or 'DIR' in i['nome'] or 'PED' in i['nome'] or 'ENF' in i['nome']:
                turma = ('Ensino Superior')
        if i['periodoLetivo']['descricao'] in ['.Ano 2024', '.Sem2024.1']:
            for c in i['professoresDisciplinas']:
                obj_turmas.append(
                    {'turma': turma, 'nome': i['nome'],
                     'disciplina': c['disciplina']['nome']}
                )
    return obj_turmas


if __name__ == '__main__':
    teste = PlanejamentoSemanal.objects.all()
    
    for i in teste:
        print(i)