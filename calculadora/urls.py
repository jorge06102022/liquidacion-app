from django.urls import path
from .views import index, privacidad, terminos, contacto

urlpatterns = [
    path('', index, name='index'),
    path('privacidad/', privacidad, name='privacidad'),
    path('terminos/', terminos, name='terminos'),
    path('contacto/', contacto, name='contacto'),
]