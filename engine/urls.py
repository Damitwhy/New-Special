from django.urls import path
from . import views

app_name = 'engine'

urlpatterns = [
    path('', views.engine, name='engine'),
    path('create/', views.engine_create, name='create'),
]