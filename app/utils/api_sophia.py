import requests

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


if __name__ == '__main__':
    teste_1 = recurso_disciplina()
    teste_2 = teste()
    for i in teste_1:
        print(i['nome'])
