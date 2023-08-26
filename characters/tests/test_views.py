from django.test import TestCase
from django.urls import reverse
from characters.models import Character

class CharacterViewSetTestCase(TestCase):

    def setUp(self):
        self.character_1 = Character.objects.create(name='Noctis')
        self.character_2 = Character.objects.create(name='Bob')
        
    def test_character_list_statuscode_200(self):
        response = self.client.get(reverse("character-list"))
        self.assertEqual(response.status_code, 200)

    def test_character_retrieve_statuscode_200(self):
        response = self.client.get(reverse("character-detail", args=[self.character_1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Noctis')

    def test_number_of_character_entries(self):
        response = self.client.get(reverse("character-list"))
        self.assertEqual(len(response.data), 2)

    def test_number_of_data_fields(self):
        response = self.client.get(reverse("character-detail", args=[self.character_1.id]))
        self.assertEqual(len(response.data), 5)