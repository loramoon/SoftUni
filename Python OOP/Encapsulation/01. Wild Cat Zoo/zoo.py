class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        has_money = self.__budget >= price
        has_capacity = self.__animal_capacity != len(self.animals)
        if has_money and has_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if not has_money and has_capacity:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity != len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_money = 0
        for animal in self.animals:
            total_care_money += animal.money_for_care
        if self.__budget >= total_care_money:
            self.__budget -= total_care_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        info = {"Lion": [], "Tiger": [], "Cheetah": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.animals]

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(info['Lion'])} Lions:",
            *info['Lion'],
            f"----- {len(info['Tiger'])} Tigers:",
            *info['Tiger'],
            f"----- {len(info['Cheetah'])} Cheetahs:",
            *info['Cheetah']
        ]

        return '\n'.join(str(r) for r in result)

    def workers_status(self):
        info = {"Caretaker": [], "Vet": [], "Keeper": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info['Keeper'],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info['Caretaker'],
            f"----- {len(info['Vet'])} Vets:",
            *info['Vet']
        ]

        return '\n'.join(result)
