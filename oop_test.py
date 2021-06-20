class Pet:

    def __init__(self, name, breed, year_of_birth, owner=None):  # owner: User = None
        self.name = name
        self.breed = breed
        self.year_of_birth = year_of_birth
        self.owner = owner

    def __str__(self):
        return f"{self.name} the {self.breed} "


class User:
    def __init__(self, name, surname, address, phone,
                 pets: list[Pet] = []):  # default arg value is mutable - что с этим делать?
        self.name = name
        self.surname = surname
        self.address = address
        self.phone = phone
        self.pets = pets
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


man = User("Sherlock", "Holmes", "221b, Baker street, London", "(020) 1234 5678")
dog = Pet("Jacky", "Нound", 1990)
cat = Pet("Betty", "Сat", 1999)

print(man)
man += dog
man += cat
# Как лучше определять геттеры и сеттеры: через аннотации или методы get/set?
# Так, например, читая код, не понимаешь сразу, приватный это атрибут или нет
man.password = "qwerty"
print(man)
print(f"{cat}. Owner: {cat.owner} {cat.owner.surname}")
print(man.password)
