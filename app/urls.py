from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_suenos, name='lista_suenos'),
    path('nuevo/', views.registrar_sueno, name='registrar_sueno'),
]
