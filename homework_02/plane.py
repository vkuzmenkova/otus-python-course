from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


class Plane(Vehicle):

    # добавьте атрибуты cargo и max_cargo классу Plane ?
    # cargo = 0
    # max_cargo = 1000

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        # super(Plane, self).__init__(weight, fuel, fuel_consumption) как правильно вызвать конструктор?
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo_weight):

        if self.cargo + cargo_weight <= self.max_cargo:
            self.cargo += cargo_weight
        else:
            raise CargoOverload("Cargo is too heavy.")

    def remove_all_cargo(self):

        current_cargo = self.cargo
        self.cargo = 0

        return current_cargo
