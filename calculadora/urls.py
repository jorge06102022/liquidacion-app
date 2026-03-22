from django.urls import path
from .views import index
from . import views


urlpatterns = [
    path('', index, name='index'),
        path('privacidad/', views.privacidad, name='privacidad'),
        path('terminos/', views.terminos, name='terminos'),
        path('contacto/', views.contacto, name='contacto'),
]