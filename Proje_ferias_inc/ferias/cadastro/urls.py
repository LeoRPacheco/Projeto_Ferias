from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name="cadastro"),
    path('atualiza_cadastro/', views.att_cadastro, name="atualiza_cadastro")

]