from django.contrib import admin
from django.urls import path, include
from app.urls.urlsEstoque import urlpatterns as urlEstoque
from app.urls.urlsLogin import urlpatterns as urlLogin
from app.urls.urlsCompra import urlpatterns as urlCompras
from app.urls.urlsUsuario import urlpatterns as urlUsuario
from app.urls.urlsEmpresa import urlpatterns as urlEmpresa
from app.urls.urlsDashboard import urlpatterns as urlDashboard
from app.urls.urlsFinancas import urlpatterns as urlFinancas


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urlLogin)),
    path('estoque/',include(urlEstoque)),
    path('compras/',include(urlCompras)),
    path('usuario/',include(urlUsuario)),
    path('empresa/',include(urlEmpresa)),
    path('dashboard/',include(urlDashboard)),
    path('financas/',include(urlFinancas)),
]