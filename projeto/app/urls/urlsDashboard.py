from django.urls import path
from app.views import viewsDashboard

urlpatterns = [
    path('dashboard', viewsDashboard.dashboard, name='dashboard'),
]
