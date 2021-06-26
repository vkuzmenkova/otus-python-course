from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo_weight):
        """
        Добавляет на самолет груз, если он не превышает ограничение по весу.
        """
        if self.cargo + cargo_weight <= self.max_cargo:
            self.cargo += cargo_weight
        else:
            raise CargoOverload("Cargo is too heavy.")

    def remove_all_cargo(self):
        """
        Опустошает грузовое отделение и возвращает вес удаленного груза.
        """
        current_cargo = self.cargo
        self.cargo = 0

        return current_cargo

