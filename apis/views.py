from rest_framework import viewsets
from characters.models import Character
from characters.serializers import CharacterSerializer

class CharacterViewset(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer