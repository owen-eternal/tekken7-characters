from django.urls import reverse
from characters.models import Character
from rest_framework.test import APITestCase
from rest_framework import status

class CharacterViewSetTestCase(APITestCase):

    def setUp(self):
        character_1 = Character.objects.create(name='Noctis')
        character_2 = Character.objects.create(name='Bob')
        
    def test_character_list_statuscode_200(self):
        response = self.client.get(reverse("character-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_character_retrieve_statuscode_200(self):
        response = self.client.get(reverse("character-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Noctis')

    def test_number_of_character_entries(self):
        response = self.client.get(reverse("character-list"))
        self.assertEqual(len(response.data), 2)