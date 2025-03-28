from django.urls import path
from app.views import viewsCompras
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('venda/', viewsCompras.index, name='venda'),
    path('dashboardVendas/', viewsCompras.estatisticasVendas,name='dashboardVendas'),
    path('devolucao/',viewsCompras.devolucao, name='devolucao'),
]
