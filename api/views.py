from django.db import transaction
from django.db.models import Q
from .models import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
import json
from .helpers import obtenerUsuario, respuesta, error, crearSerializador
from .const import *

@method_decorator(csrf_exempt, name='dispatch')
class GestionarUsuario(View):
    
    def post(self, request):
        try:
            dataRequest = JSONParser().parse(request)
            serializador = crearSerializador(Usuario, 0)
            nuevoUsuario =  serializador(Usuario.__nuevo__(dataRequest['username'],dataRequest['password'],dataRequest['first_name'],dataRequest['email'],dataRequest['telefono'],dataRequest['es_proveedor'],dataRequest['is_staff'], imagen), many = False).data
            return respuesta(nuevoUsuario)
        except BaseException as err:
            return error(str(err))
        
    def get(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            serializador = crearSerializador(Usuario, 0)
            return respuesta(serializador(Usuario.objects.filter(id = usuario.id), many = True).data)
            # usuario = obtenerUsuario(request)
            # if usuario == None:
            #     return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            # serializador = crearSerializador(Usuario, 0)
            # if request.body:
            #     datosRequest = json.loads(request.body.decode('utf-8'))
            #     usuarios = serializador(Usuario.objects.filter(id = datosRequest.get('id')), many = True).data 
            # else: 
            #     usuarios = serializador(Usuario.objects.all(), many = True).data
            #return respuesta(usuarios)
        except BaseException as err:
            return error(str(err))
        
    def put(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            imagen = Base64Aimagen(dataRequest['imagen'])
            serializador = crearSerializador(Usuario, 0)
            usuarioActualizado =  serializador(Usuario.__actualizar__(usuario,dataRequest['username'],dataRequest['password'],dataRequest['first_name'],dataRequest['email'],dataRequest['telefono'],dataRequest['es_proveedor'],dataRequest['is_staff'], imagen, dataRequest['imagenB64']), many = False).data
            return respuesta(usuarioActualizado)
        except BaseException as err:
            return error(str(err))
        
    def delete(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            serializador = crearSerializador(Usuario, 0)
            usuarioInhabilitado =  serializador(Usuario.__inhabilitar__(usuario), many = False).data
            return respuesta(usuarioInhabilitado)
        except BaseException as err:
            return error(str(err))

@csrf_exempt       
def recibirDatos(request):
    try:
        with transaction.atomic(): 
            usuario = obtenerUsuario(request)
            if usuario == None:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            nuevaC =  Configuracion.__nueva__(dataRequest['datos']['configuracion'])
            jugadas = []
            for item in dataRequest['datos']['jugadas']:
                nueva =  Jugada.__nueva__(item)
                jugadas.append(nueva)
            if not usuario.configuracionActualizada:
                serializer = crearSerializador(Configuracion, 0)
                confGlobal = serializer(Configuracion.objects.get(usuario="global"), many = False).data
                usuario.configuracionActualizada = True
                usuario.save()
                return respuesta(confGlobal)
            return respuesta("OK")
    except BaseException as err:
        return error(str(err))

@csrf_exempt       
def enviarDatos(request):
    try:
        # usuario = obtenerUsuario(request)
        # if usuario == None:
        #     return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
        with transaction.atomic(): 
            serializadorC = crearSerializador(Configuracion, 0)
            serializadorJ = crearSerializador(Jugada, 0)
            dataC = serializadorC( Configuracion.objects.filter(enviado=False), many = True).data
            dataJ = serializadorJ(Jugada.objects.filter(enviado=False), many = True).data
            Configuracion.objects.filter(enviado=False).update(enviado=True)
            Jugada.objects.filter(enviado=False).update(enviado=True)
            return respuesta({"configuraciones": dataC,"jugadas":dataJ})
    except BaseException as err:
        return error(str(err))

@csrf_exempt       
def recibirConfiguracionGlobal(request):
    try:
        with transaction.atomic(): 
            usuario = obtenerUsuario(request)
            if usuario == None:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            Configuracion.objects.filter(usuario="global").delete()
            datos = dataRequest['datos']['configuracion']
            datos["usuario"] = "global"
            nuevaC =  Configuracion.__nueva__(datos)
            Usuario.objects.all().update(configuracionActualizada = False)
            return respuesta("OK")
    except BaseException as err:
        return error(str(err))

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return respuesta({
            'token': token.key,
        })