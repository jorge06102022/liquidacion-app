from django.urls import path
from .views import index, privacidad, terminos, contacto, calcular_prima, home, calcular_cesantias, calcular_vacaciones

urlpatterns = [
    path('index/', index, name='index'),
    path('privacidad/', privacidad, name='privacidad'),
    path('terminos/', terminos, name='terminos'),
    path('contacto/', contacto, name='contacto'),

    path('prima/', calcular_prima, name='prima'),
    path('', home, name='home'),
    path('cesantias/', calcular_cesantias, name='cesantias'),
    path('vacaciones/', calcular_vacaciones, name='vacaciones'),
]