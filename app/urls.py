from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.redirect_user, name='home'),
    path('inicio/', views.pagina_inicial, name='profile'),  # noqa: E501
    path('inicio/<str:username>/escolher_curso_para_o_planejamento_semanal/', views.escolher_curso_para_planejamento_semanal, name='escolher_curso_para_planejamento_semanal'),  # noqa: E501
    path('inicio/<str:username>/planejamento_semanal/<int:turma>', views.planejamento_semanal, name='planejamento_semanal'),  # noqa: E501
    path('inicio/<str:username>/meus_planejamentos/', views.meus_planejamentos, name='meus_planejamentos'),  # noqa: E501
]
