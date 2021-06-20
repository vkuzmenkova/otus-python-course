from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    # добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию ?
    # добавьте инициализатор для установки weight, fuel, fuel_consumption

    # weight = 1000
    # started = False
    # fuel = 0
    # fuel_consumption = 1

    def __init__(self, weight=1000, fuel=0, fuel_consumption=1):
        # на выполнение тестов влияет порядок аргументов?
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):

        if not self.started and self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError('Low fuel.')

    def move(self, distance):

        fuel_needed = distance * self.fuel_consumption

        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
        else:
            raise NotEnoughFuel('More fuel needed')

# car = Vehicle(100, 1, 1)
# car.start()  # печатается 2 раза?
# car.move(1)
