class Validator:

    @staticmethod
    def no_valid_name(name, message):
        if name.strip() == '':
            raise ValueError(message)

    @staticmethod
    def no_valid_price(price, message):
        if price <= 0:
            raise ValueError(message)

    @staticmethod
    def find_aquarium(aquarium_name, aquariums):
        for aquarium in aquariums:
            if aquarium.name == aquarium_name:
                return aquarium


