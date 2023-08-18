from django.contrib import admin
from .models import Profile, Character, Ability, Specialty

admin.site.register(Character)
admin.site.register(Profile)
admin.site.register(Ability)
admin.site.register(Specialty)
