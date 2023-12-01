from django.contrib import admin
from .models import Musica, Album
from .models import Banda, Album
from .forms import *
from app.models import *

class MusicaInline(admin.TabularInline):

    model = Musica
    form = MusicaForm
    extra = 1


class AlbumInline(admin.TabularInline):

    model = Album
    form = AlbumForm
    extra = 1

# classe para exibir as musicas
class AlbumAdmin(admin.ModelAdmin):
    # atributo inline para exibir as musicas inline xD
    inlines = [MusicaInline]

# classe para exibir as bandas
class BandaAdmin(admin.ModelAdmin):
    # atributo inline para exibir as bandas inline xD
    inlines = [AlbumInline]

# com o inline não precisamos registrar o model Album
admin.site.register(Musica),
admin.site.register(Banda, BandaAdmin),
# admin.site.register(Album),

# Register your models here.
admin.site.register(Funcoes)
admin.site.register(Pessoa)

admin.site.register(Genero)

admin.site.register(Album,AlbumAdmin)
admin.site.register(Cadastro)
admin.site.register(Biagrafia)
admin.site.register(apresentacao)

