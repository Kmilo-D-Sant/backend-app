from django.urls import path
from api.views import *
from rest_framework.authtoken import views

app_name = 'api'

urlpatterns = [
    path('enviar-datos', recibirDatos, name="enviar-datos"),
    path('enviar-datos/', recibirDatos, name="enviar-datos"),
    path('recibir-datos', enviarDatos, name="recibir-datos"),
    path('recibir-datos/', enviarDatos, name="recibir-datos"),
    path('recibir-configuracion-global', recibirConfiguracionGlobal, name="'recibir-configuracion-global"),
    path('recibir-configuracion-global/', recibirConfiguracionGlobal, name="'recibir-configuracion-global"),
    path('recibir-token', CustomAuthToken.as_view()),
    path('recibir-token/', CustomAuthToken.as_view()),
    path('', bienvenido, name="bienvenido"),
    #path('notificar', notificar, name="notificar"),

    ]