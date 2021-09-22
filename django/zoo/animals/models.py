from django.db import models


# Create your models here.
class AnimalKind(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField(verbose_name='about')

    def __str__(self):
        return f"{self.name}"


class Animal(models.Model):
    name = models.CharField(max_length=64, blank=True, unique=False)  # blank на уровне валидации строк
    kind = models.ForeignKey(AnimalKind, on_delete=models.CASCADE,
                             related_name='get_animals')  # kind1.get_animals.all() = kind1.<modelname - animal_set>.all(), should be unique!
    age = models.PositiveSmallIntegerField(null=True)  # null - на уровне бд

    def __str__(self):
        return f"{self.name} the {self.kind}"


class AnimalProfile(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)
    desc = models.TextField(verbose_name='about')

    def __str__(self):
        return f"{self.animal.name}'s bio: {self.desc}"


class Food(models.Model):
    name = models.CharField(max_length=64)
    kinds = models.ManyToManyField(AnimalKind)
