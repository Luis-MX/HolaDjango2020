
from django.contrib import admin
from django.urls import path
from hola.views import def_hola, def_login, def_articulo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', def_hola),
    path('login/', def_login),
    path('articulo/', def_articulo),
]
