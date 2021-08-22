from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.index),
    path('prova/', views.prova),
    path('opcao/', views.opcao),
    path('hook/', views.talkin_to_me_bruh),
]
