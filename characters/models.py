from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Profile(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    description = models.TextField()

    def __str__(self):
        return f'Profile for: {self.character.name}'

class Ability(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, primary_key=True, related_name='ability')
    combo_damage = models.IntegerField()
    mobility = models.IntegerField()
    wall_carry = models.IntegerField()
    throw_game = models.IntegerField()

    def __str__(self):
        return f'Abilities for: {self.character.name}'

class Specialty(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='specialties')
    spec_name = models.CharField(max_length=30)
    damage = models.CharField(max_length=30)
    move_list = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Specialty for: {self.character.name}'
