from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 500
    started = False
    fuel = 0
    # в литрах на 100 км
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        """
        :param weight:
        :param fuel:
        :param fuel_consumption:
        """

        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """

        :param self:
        :return:
        """
        if not self.started and self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError('Low fuel!')

    def move(self, distance):
        """
        """
        fuel_needed = distance  * self.fuel_consumption

        if self.fuel > fuel_needed:
            self.fuel -= fuel_needed
        else:
            raise NotEnoughFuel('More fuel needed')
