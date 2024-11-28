from django.urls import path
from . import views

app_name = 'inscripciones'

urlpatterns = [
    path('inscripcion_tertulia', views.inscripcion_tertulia, name="inscripcion_tertulia"),
]