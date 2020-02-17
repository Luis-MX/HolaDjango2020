from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class TestHumo(TestCase):

    def test_prueba_humo(self):
        self.assertEqual(2 + 2, 4)