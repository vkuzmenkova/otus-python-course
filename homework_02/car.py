"""
создайте класс `Car`, наследник `Vehicle`
"""
from dataclasses import dataclass
from .base import Vehicle


class Car(Vehicle):
    engine = None

    def set_engine(self):
        pass
