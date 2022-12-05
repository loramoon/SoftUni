class Validator:

    @staticmethod
    def no_valid_name(name, message):
        if name.strip() == '':
            raise ValueError(message)

    @staticmethod
    def find_astronaut(name, astronauts):
        for astronaut in astronauts:
            if astronaut.name == name:
                return astronaut
        raise Exception(f"Astronaut {name} doesn't exist!")

    @staticmethod
    def find_planet(planet_name, planets):
        for planet in planets:
            if planet.name == planet_name:
                return planet
        raise Exception("Invalid planet name!")


