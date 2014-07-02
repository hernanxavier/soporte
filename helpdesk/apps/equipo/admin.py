# coding=utf-8
from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import EnclosedInput
from .models import *
from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin
from suit.admin import SortableTabularInline


# Register your models here.


class tipo_equipo_informaticoAdmin(admin.ModelAdmin):
    list_display = ['nombre', ]
    search_fields = ['nombre', ]
admin.site.register(tipo_equipo_informatico)


class marcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', ]
    search_fields = ['nombre', ]
admin.site.register(marca)


class equipo_informaticoAdmin(admin.ModelAdmin):
    list_display = ['numero_serio', 'tipo_equipo_informatico', 'marca']
    search_fields = ['numero_serio', 'tipo_equipo_informatico', 'marca']
admin.site.register(equipo_informatico)
