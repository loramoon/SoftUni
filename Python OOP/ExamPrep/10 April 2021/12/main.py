from project.controller import Controller

controller = Controller()
controller.aquariums = []

print(controller.add_aquarium("FreshwaterAquarium", "Aqua"))
print(controller.add_aquarium("SaltwaterAquarium", "Sea"))
print(controller.add_aquarium("Sugar", "Sea"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Stone"))
print(controller.insert_decoration("Aqua", "Plant"))
print(controller.insert_decoration("Sea", "Ornament"))
print(controller.insert_decoration("Aqua", "Ornament"))
print(controller.add_fish("Aqua", "FreshwaterFish", "Goldy", 'fish', 5))
print(controller.add_fish("Aqua", "FreshwaterFish", "BabyShark", 'shark', 105))
print(controller.add_fish("Sea", "FreshwaterFish", "Goldy", 'fish', 5))
print(controller.add_fish("Sea", "SaltwaterFish", "Goldy", 'fish', 25))
print(controller.feed_fish("Aqua"))
print(controller.feed_fish("Sea"))
print(controller.calculate_value("Aqua"))
print(controller.calculate_value("Sea"))
print(controller.report())
a= 5
