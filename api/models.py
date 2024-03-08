from django.db import models
from .helpers import error, respuesta
from datetime import datetime
from rest_framework import status
from django.contrib.auth.models import AbstractUser, User
import io
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone
from .helpers import crearSerializador


class Usuario(AbstractUser):
    telefono = models.CharField(max_length=10)
    es_proveedor = models.BooleanField("Es proveedor", default= False, null =False, blank = False)
    imagen = models.ImageField(blank= True, null= True, default="",upload_to="imagenes/")
    imagenB64 = models.TextField(blank= True, null= True)
    configuracionActualizada = models.BooleanField("Configuración actual", default= False, null =False, blank = False)
    

    def __nuevo__(username, password, first_name, email, telefono, es_proveedor, is_staff, imagen):
        self = Usuario()
        if imagen != None:
            imagen_io = io.BytesIO()
            imagen.save(imagen_io, format='PNG')
            self.imagen = InMemoryUploadedFile(imagen_io, field_name=None, name= username + ".png", content_type='imagen/png', size=imagen_io.tell, charset=None)
            
        self.username = username
        self.set_password(password)
        self.first_name = first_name
        self.email = email
        self.telefono = telefono
        self.es_proveedor = es_proveedor
        self.is_staff = is_staff
        self.imagenB64 = imagenB64
        self.save()
        return self      
    
    def __actualizar__(self, username, password, first_name, email, telefono, es_proveedor, is_staff, imagen, imagenB64):
        if imagen != None:
            imagen_io = io.BytesIO()
            imagen.save(imagen_io, format='PNG')
            self.imagen = InMemoryUploadedFile(imagen_io, field_name=None, name= username + ".png", content_type='imagen/png', size=imagen_io.tell, charset=None)
        self.username = username
        self.set_password(password)
        self.first_name = first_name
        self.imagenB64 = imagenB64
        self.email = email
        self.telefono = telefono
        self.es_proveedor = es_proveedor
        self.is_staff = is_staff
        self.save()
        return self     
     
    def __inhabilitar__(self):
        self.is_active = False
        self.save()
        return self 
    
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"


class Jugada(models.Model):
    tipo = models.CharField("Tipo", max_length=50, blank=False, null=False)
    usuario = models.CharField("Usuario", max_length=50, blank=False, null=False)
    numeros = models.CharField("Numeros", max_length=100, blank=False, null=False)
    montoFijo = models.FloatField(default=0)
    montoCorrido = models.FloatField(default=0)
    enElBote = models.BooleanField(default=False)
    fecha = models.BigIntegerField(default=0)
    tiroManana =models.BooleanField(default=True)
    premio = models.FloatField(default=0)
    enviado =models.BooleanField(default=False)
    
    def __nueva__(data):
        serializador = crearSerializador(Jugada, 0)
        serializer = serializador(data=data)
        if serializer.is_valid(raise_exception=True):
            objectAux = serializer.save()
            return objectAux
        else:
            return None
        
    # def __nueva__( tipo,  numeros,  monto,  enElBote,  corrido,  usuario, fecha, tiroManana):
    #     self =  Jugada()
    #     self.tipo = tipo
    #     self.usuario = usuario
    #     self.numeros = numeros
    #     self.montoFijo = monto
    #     if tipo == TipoJugada.BOLA:
    #         self.montoCorrido = corrido
    #     self.enElBote = enElBote
    #     self.fecha = fecha
    #     self.tiroManana = tiroManana
    #     self.save()
    #     return self
        

class Configuracion(models.Model):
    usuario = models.CharField( max_length=100, blank=False, null=False)
    fecha = models.BigIntegerField(default=0)
    horaAperturaDia = models.CharField( max_length=20, blank=False, null=False)
    horaAperturaDia = models.CharField( max_length=20, blank=False, null=False, default= "06:00:00")
    horaCierreDia = models.CharField( max_length=20, blank=False, null=False, default= "13:15:00")
    horaAperturaNoche = models.CharField( max_length=20, blank=False, null=False, default= "14:00:00")
    horaCierreNoche = models.CharField( max_length=20, blank=False, null=False, default= "21:20:00")
    beneficioCliente = models.FloatField(default=0.3)
    beneficioClienteBote = models.FloatField(default=0.1)
    beneficioClienteBola = models.FloatField(default=0.2)
    beneficioClienteBolaBote = models.FloatField(default=0.1)
    pagoFijo = models.IntegerField(default=75)
    pagoFijoBote = models.IntegerField(default=80)
    pagoFijoLimitado = models.IntegerField(default=50)
    pagoFijoLimitadoBote = models.IntegerField(default=50)
    pagoCorrido = models.IntegerField(default=25)
    pagoCorridoBote = models.IntegerField(default=20)
    pagoCorridoLimitado = models.IntegerField(default=20)
    pagoCorridoLimitadoBote = models.IntegerField(default=20)
    pagoParlet = models.IntegerField(default=1100)
    pagoParletBote = models.IntegerField(default=1000)
    pagoParletLimitado = models.IntegerField(default=500)
    pagoParletLimitadoBote = models.IntegerField(default=500)
    pagoCentena = models.IntegerField(default=400)
    pagoCentenaLimitado = models.IntegerField(default=200)
    pagoCentenaBote = models.IntegerField(default=400)
    pagoCentenaLimitadoBote = models.IntegerField(default=200)
    topeFijo = models.IntegerField(default=200)
    topeFijoBote = models.IntegerField(default=400)
    topeFijoUsuario = models.IntegerField(default=200)
    topeFijoBoteUsuario = models.IntegerField(default=400)
    topeCorrido = models.IntegerField(default=100)
    topeCorridoBote = models.IntegerField(default=200)
    topeCorridoUsuario = models.IntegerField(default=100)
    topeCorridoBoteUsuario = models.IntegerField(default=200)
    topeCentena = models.IntegerField(default=1000)
    topeCentenaBote = models.IntegerField(default=200)
    topeCentenaUsuario = models.IntegerField(default=100)
    topeCentenaBoteUsuario =models.IntegerField(default=200) 
    topeParlet = models.IntegerField(default=10)
    topeParletBote = models.IntegerField(default=20)
    topeParletUsuario = models.IntegerField(default=10)
    topeParletBoteUsuario = models.IntegerField(default=20)
    tiroManana = models.BooleanField(default=True)
    limitadosBola = models.CharField( max_length=100, blank=False, null=False)
    limitadosBolaBote = models.CharField( max_length=100, blank=False, null=False)
    limitadosBolaUsuario = models.CharField( max_length=100, blank=False, null=False)
    limitadosBolaBoteUsuario = models.CharField( max_length=100, blank=False, null=False)
    limitadosParlet = models.CharField( max_length=100, blank=False, null=False)
    limitadosParletUsuario = models.CharField( max_length=100, blank=False, null=False)
    limitadosParletBote = models.CharField( max_length=100, blank=False, null=False)
    limitadosParletBoteUsuario = models.CharField( max_length=100, blank=False, null=False)
    limitadosCentena = models.CharField( max_length=100, blank=False, null=False)
    limitadosCentenaUsuario = models.CharField( max_length=100, blank=False, null=False)
    limitadosCentenaBote = models.CharField( max_length=100, blank=False, null=False)
    limitadosCentenaBoteUsuario = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaBola = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaBolaBote = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaBolaUsuario = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaBolaBoteUsuario = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaParlet = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaParletBote = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaParletUsuario = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaParletBoteUsuario = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaCentena = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaCentenaBote = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaCentenaUsuario = models.CharField( max_length=100, blank=False, null=False)
    noSeJuegaCentenaBoteUsuario = models.CharField( max_length=100, blank=False, null=False)
    enviado =models.BooleanField(default=False)
    
    def __nueva__(data):
        serializador = crearSerializador(Configuracion, 0)
        serializer = serializador(data=data)
        if serializer.is_valid(raise_exception=True):
            objectAux = serializer.save()
            return objectAux
        else:
            return None

