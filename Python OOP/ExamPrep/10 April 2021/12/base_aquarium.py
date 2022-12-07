from abc import ABC, abstractmethod
from project.validator import Validator


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.no_valid_name(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish):
        if fish.__class__.__name__ in ("FreshwaterFish", "SaltwaterFish"):
            if self.capacity != len(self.fish):
                self.fish.append(fish)
                return f"Successfully added {fish.__class__.__name__} to {self.name}."
            return "Not enough capacity."

    def remove_fish(self, fish):
        for a_fish in self.fish:
            if a_fish.name == fish.name:
                self.fish.remove(a_fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for a_fish in self.fish:
            a_fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        if not self.fish:
            result += 'Fish: none\n'
        else:
            result += f"Fish: {' '.join(fish.name for fish in self.fish)}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}\n"
        return result.strip()




