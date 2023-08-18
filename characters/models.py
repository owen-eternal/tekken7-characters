from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Profile(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return f'Profile for: {self.character.name}'

class Ability(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, primary_key=True)
    combo_damage = models.IntegerField()
    mobility = models.IntegerField()
    wall_carry = models.IntegerField()
    throw_game = models.IntegerField()

    def __str__(self):
        return f'Abilities for: {self.character.name}'
