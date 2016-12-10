from __future__ import unicode_literals, print_function

from django.test import TestCase
from django.urls import reverse
from .views import *
import json

class ViewsTest(TestCase):
    def test_health(self):
        response = self.client.get(reverse('app:health'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')
