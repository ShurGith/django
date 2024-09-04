from django.contrib import admin
from .models import AutorDb, FraseDb


admin.site.site_header="Mi Panel de control"
admin.site.site_title="Mi sitio"
admin.site.index_title="Index"


# Register your models here.
class FraseInLine(admin.TabularInline):
    model = FraseDb
    extra = 1




class AutorAdmin(admin.ModelAdmin):
    fields = ['nombre', 'fecha_nacimiento','fecha_fallecimiento','profesion', 'nacionalidad']
    list_display = ['nombre', 'fecha_nacimiento']

    inlines = [FraseInLine]


admin.site.register(AutorDb,AutorAdmin)

@admin.register(FraseDb)
class FraseAdmin(admin.ModelAdmin):
    fields = ['cita', 'autor_fk']
    list_display = ['cita','autor_fk']