from django.urls import reverse
from characters.models import Character
from rest_framework.test import APITestCase
from rest_framework import status

class CharacterViewSetTestCase(APITestCase):

    def setUp(self):
        character_1 = Character.objects.create(name='Noctis')
        character_2 = Character.objects.create(name='Bob')