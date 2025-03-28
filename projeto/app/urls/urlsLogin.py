from django.urls import path
from app.views import viewsLogin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',viewsLogin.loginUser, name='login'),
    path('home/',viewsLogin.home, name='home'),
    path('acessoNegado/', viewsLogin.erroAcessoUrls, name='acessoNegado'),
    path('logut/', viewsLogin.logout_view, name='logout')
]