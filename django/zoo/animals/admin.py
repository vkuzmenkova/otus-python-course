from django.contrib import admin
from animals.models import Animal, AnimalProfile

# Register your models here.
admin.site.register(Animal)
admin.site.register(AnimalProfile)