import os
import requests

from google.oauth2 import service_account
from googleapiclient.discovery import build

#  CONSTANTES
PATH_CREDENTIALS = "C:\\Users\\francisco.duo\\Desktop\\portalcciProfessor\\credentials.json"
SERVICE_ACCOUNT = "francisco.duo@portalcci.com.br"
SCOPES = [
    "https://www.googleapis.com/auth/admin.directory.user",
    "https://www.googleapis.com/auth/admin.directory.group.member",
    "https://www.googleapis.com/auth/admin.directory.group",
    "https://www.googleapis.com/auth/spreadsheets"
]

SOPHIA_ACCESS = {
    "usuario": "setape",
    "senha": "setape"
}

POST_AUTH = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Autenticacao"
GET_STUDENTS = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Alunos"
GET_STUDENT = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Alunos/"
PUT_STUDENTS = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Alunos/"
GET_CLASSROOM = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Turmas"
GET_SUBJECTS = "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Disciplinas"


# CONECTAR
try:
    creds = service_account.Credentials.from_service_account_file(
        filename=PATH_CREDENTIALS,
        scopes=list(SCOPES),
        subject=SERVICE_ACCOUNT
    )

except Exception as e:
    if os.path.exists(PATH_CREDENTIALS):
        raise Exception(
            f"The file exists. Verify your connection to google api.\n{e}"
        )
    else:
        raise Exception(
            f"The crendential.json is not exist.\n{e}"
        )


def connect_to_google_admin() -> build:
    return build('admin', 'directory_v1', credentials=creds)


def connect_sophia():
    access_key = {
        "token": requests.post(
            POST_AUTH, json=SOPHIA_ACCESS
        ).text
    }

    return access_key


# RESOURCES

SERVICE = connect_to_google_admin()


def get_data_of_current_user(userkey: str) -> dict:
    return SERVICE.users().get(
        userKey=userkey,
    ).execute()


# SOPHIA

def classroom_of_sophia() -> requests:
    return requests.get(
        GET_CLASSROOM, headers=connect_sophia()
    ).json()


def subjects_of_sophia() -> requests:
    return requests.get(
        GET_SUBJECTS, headers=connect_sophia()
    ).json()


# teste = classroom_of_sophia()
# for t in teste:
#     print(t['nome'])