from django.contrib import admin

from django.contrib import admin
from django.contrib.auth import get_user_model

from api.helpers import crearSerializador
from .models import *

Usuario = get_user_model()

admin.site.register(Jugada)
admin.site.register(Configuracion)
@admin.register(Usuario)
class Usuario(admin.ModelAdmin):
    list_display  = ["username","first_name", "telefono", "es_proveedor", "is_active"]
    list_filter = ("es_proveedor", "is_active")
