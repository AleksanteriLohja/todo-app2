from django.contrib import admin

from.models import Kategoria, Tehtava


@admin.register(Tehtava)
class TehtavaAdmin(admin.ModelAdmin):
    list_display = ["id", "otsikko",]
    
@admin.register(Kategoria)
class KategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "otsikko"]
    pass