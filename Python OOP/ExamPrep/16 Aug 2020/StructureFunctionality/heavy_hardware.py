import math

from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Heavy", capacity, memory)
        self.capacity *= 2
        self.memory = math.floor(self.memory * 0.75)