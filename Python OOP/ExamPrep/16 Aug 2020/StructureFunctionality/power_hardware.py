import math

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Power", capacity, memory)
        self.capacity = math.floor(self.capacity * 0.25)
        self.memory = math.floor(self.memory * 1.75)