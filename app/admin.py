from django.contrib import admin
from .models import *  # noqa: F403


admin.site.register(Instituicao, )  # noqa: F405
admin.site.register(Serie, )  # noqa: F405
admin.site.register(Taxonomia, )  # noqa: F405
admin.site.register(Disciplina, )  # noqa: F405
admin.site.register(Turma, )  # noqa: F405
admin.site.register(PlanejamentoSemanal, )  # noqa: F405
admin.site.register(RegistroPlanejamentoSemanal, )  # noqa: F405
