from rest_framework import serializers
from .models import Character, Profile, Ability, Specialty

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['character', 'description']

class AbilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Ability
        fields = ['character', 'combo_damage', 'mobility', 'wall_carry', 'throw_game']
    
class SpecialtySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Specialty
        fields = ('character', 'spec_name', 'damage', 'move_list')

class CharacterSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(read_only=True)
    ability = AbilitySerializer(read_only=True)
    specialties = SpecialtySerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = '__all__'        