from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    # добавьте атрибут engine классу Car - почему не экземпляру ?
    engine = None

    def set_engine(self, engine: Engine):
        """
        Ставит двигатель на машину.
        """
        self.engine = engine

