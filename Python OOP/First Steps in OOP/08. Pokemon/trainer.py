class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"

        self.pokemons.append(pokemon)

        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for a_pokemon in self.pokemons:
            if a_pokemon.name == pokemon_name:
                self.pokemons.remove(a_pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        [result.append(f"- {p.pokemon_details()}") for p in self.pokemons]

        return '\n'.join(result)
