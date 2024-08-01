from django.urls import path
from . import views

app_name = 'list_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contacts'),
    path('engine/', views.engine, name='engine'),
]