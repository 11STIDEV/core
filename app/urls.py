from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.redirect_user, name='home'),
    path('profile/', views.user_dashboard_home, name='profile'),
    path('profile/planejamento-semanal/', views.user_planejamento_semanal, name='planejamento_semanal'),  # noqa: E501
    path('profile/google-classroom/', views.user_google_classroom, name='user_googleclassroom'),  # noqa: E501
]
