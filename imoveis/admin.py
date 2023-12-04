from django.contrib import admin
from .models import Usuario, Corretor, Contrato, Imovel

admin.site.register(Usuario)
admin.site.register(Corretor)
admin.site.register(Contrato)
admin.site.register(Imovel)