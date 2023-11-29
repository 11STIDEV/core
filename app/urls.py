from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.redirect_user, name='home'),
    path('profile/', views.user_dashboard_home, name='profile'),
    path('profile/planejamento-semanal/', views.user_planejamento_semanal, name='planejamento_semanal'),  # noqa: E501
]
