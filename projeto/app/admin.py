from django.contrib import admin
from .models import Usuario, Produto, Cliente


# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    ...

class ProdutoAdmin(admin.ModelAdmin):
    ...

class ClienteAdmin(admin.ModelAdmin):
   ...


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)