from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from hola.models import Articulo
from django.urls import reverse


class TestHumo(TestCase):

    def test_prueba_humo(self):
        self.assertEqual(2 + 2, 4)
    
    def test_agrega_articulo(self):
        articulo = Articulo.objects.create(
            nombre='Libro',
            precio=499.0,
            descripcion='Libro edicion 2019',
        )
        articulo_uno = Articulo.objects.first()

        self.assertEqual(articulo_uno, articulo)
    
    def test_diferentes_instancias(self):
        articulo_a = Articulo.objects.create(
            nombre='Libro',
            precio=499.0,
            descripcion='Libro edicion 2019',
        )
        articulo_b = Articulo.objects.create(
            nombre='Libro',
            precio=499.0,
            descripcion='Libro edicion 2019',
        )

        self.assertNotEqual(articulo_a, articulo_b)
    
    def test_nombre_url_hola(self):
        response = self.client.get('/hola/')
        self.assertEqual(response.status_code, 200)
    
    def test_redireccion_admin_sin_iniciar_sesion(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)
