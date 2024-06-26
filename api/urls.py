from django.urls import path
from api.views import *
from rest_framework.authtoken import views

app_name = 'api'

urlpatterns = [
    path('enviar-datos', recibirDatos, name="enviar-datos"),
    path('enviar-datos/', recibirDatos, name="enviar-datos"),
    path('recibir-datos', enviarDatos, name="recibir-datos"),
    path('recibir-datos/', enviarDatos, name="recibir-datos"),
    path('recibir-datos-cl', enviarDatosCl, name="recibir-datos-cl"),
    path('recibir-datos-cl/', enviarDatosCl, name="recibir-datos-cl"),
    path('marcar-enviados', marcarEnviados, name="marcar-enviados"),
    path('marcar-enviados/', marcarEnviados, name="marcar-enviados"),
    path('marcar-enviados-cl', marcarEnviadosCl, name="marcar-enviados-cl"),
    path('marcar-enviados-cl/', marcarEnviadosCl, name="marcar-enviados-cl"),
    path('recibir-configuracion-global', recibirConfiguracionGlobal, name="'recibir-configuracion-global"),
    path('recibir-configuracion-global/', recibirConfiguracionGlobal, name="'recibir-configuracion-global"),
    path('recibir-token', CustomAuthToken.as_view()),
    path('recibir-token/', CustomAuthToken.as_view()),
    path('', bienvenido, name="bienvenido"),
    #path('notificar', notificar, name="notificar"),

    ]