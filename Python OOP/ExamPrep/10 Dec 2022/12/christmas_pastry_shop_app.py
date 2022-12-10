from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    TYPES = {'Gingerbread': Gingerbread, 'Stolen': Stolen}
    TYPE_BOOTH = {"Open Booth": OpenBooth, 'Private Booth': PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def find_delicacy_by_name(self, name):
        for d in self.delicacies:
            if d.name == name:
                return d

    def find_booth_by_number(self, number):
        for b in self.booths:
            if b.booth_number == number:
                return b

    def find_not_reserved_for_n_people(self, people):
        for b in self.booths:
            if not b.is_reserved:
                if b.capacity >= people:
                    return b

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.find_delicacy_by_name(name):
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(self.TYPES[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.find_booth_by_number(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.TYPE_BOOTH:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(self.TYPE_BOOTH[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        if not self.find_not_reserved_for_n_people(number_of_people):
            raise Exception(f"No available booth for {number_of_people} people!")

        booth = self.find_not_reserved_for_n_people(number_of_people)
        booth.reserve(number_of_people)

        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if not self.find_booth_by_number(booth_number):
            raise Exception(f"Could not find booth {booth_number}!")
        if not self.find_delicacy_by_name(delicacy_name):
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth = self.find_booth_by_number(booth_number)
        delicacy = self.find_delicacy_by_name(delicacy_name)
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_booth_by_number(booth_number)
        bill = booth.price_for_reservation

        for d in booth.delicacy_orders:
            bill += d.price
        self.income += bill

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
