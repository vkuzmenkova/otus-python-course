# Создать класс User со следующими атрибутами:
# имя, фамилия, почтовый адрес, мобильный номер, пароль, животные
# Создать геттер и сеттер для пароля.
# Создайте класс Pet и добавьте к нему следующие атрибуты:
# кличка, порода, год рождения, хозяин (User)
# Добавьте список из Pet как атрибут экземпляра для User.
# Создайте несколько экземпляров класса User, добавьте к юзерам 1-4 домашних животных

# cannot import name 'Pet' from partially initialized module 'pet' (most likely due to a circular import)

class Pet:

    def __init__(self, name, breed, year_of_birth, owner=None):  # owner: User = None
        self.name = name
        self.breed = breed
        self.year_of_birth = year_of_birth
        self.owner = owner

    def __repr__(self):
        return f"{self.name} the {self.breed}"


class User:
    def __init__(self, name, surname, address, phone,
                 pets: list[Pet] = []):  # default arg value is mutable - что с этим делать?
        self.name = name
        self.surname = surname
        self.address = address
        self.phone = phone
        self.pets = pets
        for pet in pets:
            pet.owner = self
        self.__password = None
        # instance attribute defined outside init - все атрибуты правильно объявлять внутри init?

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if password.isalpha():
            self.__password = password
            print('Password changed.')
        else:
            raise ValueError("Wrong password format")

    def __str__(self):
        if not self.pets:
            return f"{self.name} {self.surname} from {self.address}. Call: {self.phone}."
        else:
            pet_string = ''
            for temp_pet in self.pets:
                pet_string += str(temp_pet)
            return f"{self.name} {self.surname} from {self.address}. Call: {self.phone}. " \
                   f"Owner of: {pet_string}"

    def __add__(self, other: Pet):
        other.owner = self
        self.pets.append(other)
        return self


owl = Pet("Hedwig", "Oul", 1990)
owl = Pet("Hedwig", "Oul", 1990)
man = User("Harry", "Potter", "4, Privet Drive, Little Whinging, Surrey, UK", "(020) 1234 5678", [owl])

print(owl.owner)

# print(man.password)
# man.password = "qwerty"
# print(man.password)
