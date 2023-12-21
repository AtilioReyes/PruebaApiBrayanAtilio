from django.contrib import admin
from .models import *

class ProfeAdmin(admin.ModelAdmin):
    list_display = ['nombre','correo','telefono']

admin.site.register(ProfJefe)
# Register your models here.

# Register your models here.
