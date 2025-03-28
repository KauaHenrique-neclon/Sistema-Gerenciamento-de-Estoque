from django.urls import path
from app.views import viewsEstoque
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('estoque/',viewsEstoque.estoque, name='estoque'),
    path('removerproduto/',viewsEstoque.deletarProduto, name='removerproduto'),
    path('descricao/',viewsEstoque.descricaoProduto, name='descricao'),
    path('editar/', viewsEstoque.editarProduto, name='editar'),
    path('editarInfoProduto/',viewsEstoque.editarInfoProduto, name='editarInfoProduto'),
    path('adicionar/',viewsEstoque.adicionarProdutos, name='adicionar')
]