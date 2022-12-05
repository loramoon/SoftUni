from abc import ABC, abstractmethod

from project.validator import Validator


class Astronaut(ABC):
    OXI = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.no_valid_name(value, "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    @abstractmethod
    def breathe(self):
        self.oxygen -= self.OXI
