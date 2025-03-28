from django.urls import path
from app.views import viewsFinancas

urlpatterns = [
    path('inserirFatura/',viewsFinancas.InserirFatura, name='inserirFatura'),
    path('pagamentos/', viewsFinancas.pagamentosFaturas, name='pagamentos'),
    path('verFatura/', viewsFinancas.verFaturas, name='verFatura'),
    path('descricaoFatura/',viewsFinancas.descricaoFatura,name='descricaoFatura'),
    #path('emitirNotasFiscais/',viewsFinancas.emitirNotas,name='emitirNotasFiscais'),
]