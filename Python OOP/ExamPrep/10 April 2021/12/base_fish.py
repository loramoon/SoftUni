from abc import ABC, abstractmethod

from project.validator import Validator


class BaseFish(ABC):
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.no_valid_name(value, "Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        Validator.no_valid_name(value, "Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.no_valid_price(value, "Price cannot be equal to or below zero.")
        self.__price = value

    @abstractmethod
    def eat(self):
        self.size += 5
