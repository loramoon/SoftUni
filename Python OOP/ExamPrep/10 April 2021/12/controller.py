from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.validator import Validator


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ("FreshwaterAquarium", "SaltwaterAquarium"):
            return "Invalid aquarium type."
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
        else:
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ("Ornament", "Plant"):
            return "Invalid decoration type."
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
        else:
            self.decorations_repository.add(Plant())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = Validator.find_aquarium(aquarium_name, self.aquariums)
        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ("FreshwaterFish", "SaltwaterFish"):
            return f"There isn't a fish of type {fish_type}."

        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        else:
            fish = SaltwaterFish(fish_name, fish_species, price)

        aquarium = Validator.find_aquarium(aquarium_name, self.aquariums)
        if aquarium:
            if (fish_type == "FreshwaterFish" and str(aquarium.__class__.__name__) == "SaltwaterAquarium") or \
                    (fish_type == "SaltwaterFish" and str(aquarium.__class__.__name__) == "FreshwaterAquarium"):
                return "Water not suitable."
            return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = Validator.find_aquarium(aquarium_name, self.aquariums)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = Validator.find_aquarium(aquarium_name, self.aquariums)
        if aquarium:
            value = sum(d.price for d in aquarium.decorations) + sum(f.price for f in aquarium.fish)
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'
        return result.strip()