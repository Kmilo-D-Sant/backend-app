from django.http.response import JsonResponse
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from .models import *
from django.contrib.auth import get_user_model
import io
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

def error(mensaje: str, estado=status.HTTP_400_BAD_REQUEST):
    return JsonResponse({"error": mensaje}, status=estado)

def respuesta(datos, estado=status.HTTP_200_OK):
    return JsonResponse({"datos": datos}, status=estado)

def manipularError(err):
    strTypeError = str(type(err))
    strError = str(err)
    msg = f"{strTypeError} {strError}"
    print("<manipularError>", msg)
    try:
        if strTypeError.__contains__(CHECK_NO_EXISTE):
            return error(MENSAJE_NO_EXISTE_R, status.HTTP_404_NOT_FOUND)
        elif strTypeError.__contains__(CHECK_PARSE_ERROR):
            return error(MENSAJE_NO_CUMPLE_REQUISITOS_ESTABLECIDOS, status.HTTP_406_NOT_ACCEPTABLE)
        elif strTypeError.__contains__(CHECK_KEY_ERROR):
            return error(f'{MENSAJE_PARAMETRO_NO_VALIDO} ({strError})', status.HTTP_406_NOT_ACCEPTABLE)
        elif strTypeError.__contains__(CHECK_TYPE_ERROR):
            if strError.find(': ', 0) != -1:
                p = strError.index(': ')
                if p >= 0:
                    strError = strError[p+2:]
            return error(f'{MENSAJE_PARAMETRO_NO_VALIDO} ({strError})', status.HTTP_406_NOT_ACCEPTABLE)
        elif strTypeError.__contains__(CHECK_VALIDATION_ERROR):
            return error(f'{MENSAJE_PARAMETRO_NO_VALIDO} ({strError})', status.HTTP_406_NOT_ACCEPTABLE)
        return error(msg)
    except BaseException as otroError:
        return error(f"{str(type(otroError))} {str(otroError)}")

def extraerToken(request):
    try:
        tokenKey = str(request.META["HTTP_AUTHORIZATION"])
        if not tokenKey.find('Bearer ', 0) == -1:
            p = tokenKey.index('Bearer ')
            tokenKey = tokenKey[p+7:]
        if not tokenKey.find('Token ', 0) == -1:
            p = tokenKey.index('Token ')
            tokenKey = tokenKey[p+6:]
        return tokenKey
    except:
        return None

def obtenerObjetoSerializado(modelo, objeto=None, objetos=None, profundidad=0):
    many = False
    if objetos != None:
        objeto = objetos
        many = True
    serializador = crearSerializador(modelo, profundidad)
    return serializador(instance=objeto, many=many)

def obtenerUsuario(request):
    tokenKey = extraerToken(request)
    try:
        token = Token.objects.get(key=tokenKey)
    except:
        return None
    return obtenerObjeto(get_user_model(), token.user_id)

def obtenerObjeto(modelo, objetoId):
    try:
        return modelo.objects.get(id=objetoId)
    except BaseException as err:
        manipularError(err)
        return None

def crearSerializador(modelo, profundidad=0):
    class serializador(serializers.ModelSerializer):
        class Meta:
            model = modelo
            fields = '__all__'
            depth = profundidad

    return serializador


CHECK_ERROR = "error"
CHECK_DATOS = "datos"
CHECK_NO_EXISTE = "DoesNotExist"
CHECK_PARSE_ERROR = "ParseError"
CHECK_KEY_ERROR = "KeyError"
CHECK_TYPE_ERROR = "TypeError"
CHECK_VALIDATION_ERROR = "ValidationError"
MENSAJE_NO_EXISTE_R = "No existe el elemento solicitado"
MENSAJE_NO_EXISTE_M = "No existe el modelo solicitado"
MENSAJE_NO_CUMPLE_REQUISITOS_ESTABLECIDOS = "Los datos no cumplen con los requisitos establecidos"
MENSAJE_USUARIO_NO_AUTENTICADO = "Usuario no autenticado"
MENSAJE_USUARIO_NO_AUTORIZADO = "Usuario no autorizado"
MENSAJE_PARAMETRO_NO_VALIDO = "Parámetro no válido"
MENSAJE_AUTENTICACION_NO_VALIDA = "Usuario o contraseña incorrecta"
MENSAJE_OK = "Acción completada correctamente"
MENSAJE_ARCHIVO_NO_VALIDO = "Archivo no válido"