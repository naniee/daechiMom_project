from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.filter, name='filter'),
    path('input', views.input, name='input'),
    path('output', views.output, name='output'),
]
