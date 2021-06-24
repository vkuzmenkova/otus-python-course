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

    def __init__(self, name, surname, address, phone, muppet: Pet, password=None,
                 pets=None):  # default arg value is mutable - что с этим делать?
        if pets is None:
            pets = []
        self.name = name
        self.surname = surname
        self.address = address
        self.phone = phone
        self.pets = pets
        self.mypet = muppet
        for pet in pets:
            pet.owner = self
        self.__password = password


    # @property
    # def pets(self):
    #     return self.pets
    #
    # @pets.setter
    # def pets(self, pet_list: list[Pet]):
    #     self.pets = pet_list
    #     for pet in pet_list:
    #         pet.owner = self

    @property
    def password(self):
        if self.__password is None:
            print('Password is not set.')
        else:
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
                pet_string += str(temp_pet) + ' '
            return f"{self.name} {self.surname} from {self.address}. Call: {self.phone}. " \
                   f"Owner of: {pet_string}"

    def __add__(self, other: Pet):
        other.owner = self
        self.pets.append(other)
        return self


owl = Pet("Hedwig", "Owl", 1990)
cat = Pet("Crookshanks", "Cat", 2000)
rat = Pet("Scabbers", "Rat", 2001)
man = User("Harry", "Potter", "4, Privet Drive, Little Whinging, Surrey, UK", "(020) 1234 5678", None, [owl])

# man.pets.append(cat)
# print(man)
# print(cat.owner)  # ??
#
# redhead_man += rat
# print(redhead_man)
# print(rat.owner)
#
# print(man.password)
# man.password = "qwerty"
# print(man.password)

list_of_pets = [owl, cat]
redhead_man = User("Ron", "Weasley", "Burrow, UK", "(020) 8765 4321", "1234")
redhead_woman = User("Jeanny", "Weasley", "Burrow, UK", "(020) 8765 4321", "1234")

print(id(redhead_man.pets))
print(id(redhead_woman.pets))
