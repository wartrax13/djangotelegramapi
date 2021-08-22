from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.index),
    path('prova/', views.prova)
]
