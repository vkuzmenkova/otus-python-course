"""
создайте класс `Car`, наследник `Vehicle`
"""
from dataclasses import dataclass
from .base import Vehicle
from .engine import Engine


class Car(Vehicle):
    engine = None

    def set_engine(self, engine):
        self.engine = engine
