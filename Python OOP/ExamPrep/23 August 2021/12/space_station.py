from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.validator import Validator
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository

class SpaceStation:
    successful_missions = 0
    unsuccessful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type not in ('Biologist', 'Geodesist', 'Meteorologist'):
            raise Exception("Astronaut type is not valid!")

        if astronaut_type == "Biologist":
            self.astronaut_repository.add(Biologist(name))
        elif astronaut_type == "Geodesist":
            self.astronaut_repository.add(Geodesist(name))
        else:
            self.astronaut_repository.add(Meteorologist(name))

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = Validator.find_astronaut(name, self.astronaut_repository.astronauts)
        self.astronaut_repository.astronauts.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        best_astronauts = {}
        astro_on_mission = 0

        planet = Validator.find_planet(planet_name, self.planet_repository.planets)

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                best_astronauts[astronaut] = astronaut.oxygen
        if not best_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")
        going_out = dict(sorted(best_astronauts.items(), key=lambda item: item[1], reverse=True))

        for astronaut in going_out.keys():
            if not planet.items or astro_on_mission == 5:
                break
            while astronaut.oxygen > 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            astro_on_mission += 1

        if not planet.items:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {astro_on_mission} astronauts participated in collecting items."
        self.unsuccessful_missions += 1
        return "Mission is not completed."

    def report(self):
        result = f"{self.successful_missions} successful missions!\n" \
                 f"{self.unsuccessful_missions} missions were not completed!\n" \
                 f"Astronauts' info:\n"

        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}\n" \
                   f"Oxygen: {astronaut.oxygen}\n"
            if not astronaut.backpack:
                result += f"Backpack items: none\n"
            else:
                result += f"Backpack items: {', '.join(astronaut.backpack)}\n"
        return result
