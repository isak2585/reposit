from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.main, name='main'),
    path('index/', views.index, name="index"),
    path('membres/', views.membres, name="membres"),
    path('membres/details/<int:id>', views.details, name="details"),
]

