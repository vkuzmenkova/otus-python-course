from faker import Faker

fake = Faker('ru_RU')

print(fake.email())

print(fake.country())

print(fake.name())

print(fake.text())

print(fake.latitude(), fake.longitude())

print(fake.url())

print(fake.profile())
