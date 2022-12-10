from project.booths.booth import Booth


class OpenBooth(Booth):
    type_booth = "Open Booth"

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        if not self.is_reserved:
            self.price_for_reservation = 2.5 * number_of_people
            self.is_reserved = True
