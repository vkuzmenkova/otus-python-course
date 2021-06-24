from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=1000, fuel=0, fuel_consumption=1):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        """
        Запускает движение транспортного средства, если достаточно топлива.
        """
        if not self.started and self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError("Low fuel.")

    def move(self, distance):
        """
        Изменяет уровень топлива в транспортном средстве на значение,
        необходимое чтобы проехать заданную дистанцию.
        """
        fuel_needed = distance * self.fuel_consumption

        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
        else:
            raise NotEnoughFuel("Not enough fuel.")
