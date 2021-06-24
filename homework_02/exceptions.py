"""
???
exception Exception
All built-in, non-system-exiting exceptions are derived from this class.
All user-defined exceptions should also be derived from this class.
"""


class LowFuelError(Exception):
    pass


class NotEnoughFuel(Exception):
    pass


class CargoOverload(Exception):
    pass
