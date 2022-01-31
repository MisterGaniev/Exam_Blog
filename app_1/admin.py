from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

# Register your models here.


@admin.register(Maqola)
class Maqola_admin(ModelAdmin):
    pass