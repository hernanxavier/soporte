# coding=utf-8

from django.db import models

#from smart_selects.db_fields import GroupedForeignKey
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.contrib.auth.models import User, Group
#from django.conf import settings
#from sistema.thumbs import ImageWithThumbsField


# Create your models here.

class tipo_equipo_informatico(models.Model):
    """
    Clase para almacenar los diferentes tipos de equipos informaticos

    """
    nombre = models.CharField(max_length=255, unique=True, blank=True, null=True)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Tipo de equipos Informáticos"

    def __unicode__(self):
        return "%s" % self.nombre


class marca(models.Model):
    """
    Almacena marcas de equipos informaticos
    """
    nombre = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Marcas de equipos informáticos"

    def __unicode__(self):
        return "%s" % self.nombre


class equipo_informatico(models.Model):
    """
    Clase que guarda una lista de todos equipos informaticos del IAEN
    """

    numero_serie = models.CharField(max_length=255, unique=True, blank=True, null=True)
    tipo_equipo_informatico = models.ForeignKey(tipo_equipo_informatico)
    marca = models.ForeignKey(marca)
    modelo = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Equipos Informáticos IAEN"

    def __unicode__(self):
        return "%s" % self.tipo_equipo_informatico


