"""
создайте класс `Plane`, наследник `Vehicle`

"""

from homework_02.exceptions import CargoOverload
from .base import Vehicle

class Plane(Vehicle):

    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo


    def load_cargo(self, cargo_weight):
         """

         :param cargo_weight:
         :return: nothing
         """
         if self.cargo + cargo_weight < self.max_cargo:
            self.cargo += cargo_weight
         else:
             raise CargoOverload("Not enough space for this cargo")

    def remove_all_cargo(self):

        """
        returns weight of the removed cargo
        :return:
        """
        current_cargo = self.cargo
        self.cargo = 0

        return current_cargo