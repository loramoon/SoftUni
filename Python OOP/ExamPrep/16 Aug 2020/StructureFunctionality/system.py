from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_software = PowerHardware(name, capacity, memory)
        System._hardware.append(power_software)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(express_software)
                System._software.append(express_software)
                return
        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                light_software = LightSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(light_software)
                System._software.append(light_software)
                return
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                for software in System._software:
                    if software.name == software_name:
                        hardware.uninstall(software)
                        System._software.remove(software)
                        return
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_s_memory = 0
        total_s_capacity = 0
        total_h_memory = 0
        total_h_capacity = 0

        for software in System._software:
            total_s_memory += software.memory_consumption
            total_s_capacity += software.capacity_consumption

        for hardware in System._hardware:
            total_h_memory += hardware.memory
            total_h_capacity += hardware.capacity

        result = "System Analysis\n" \
                 f"Hardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {total_s_memory} / {total_h_memory}\n" \
                 f"Total Capacity Taken: {total_s_capacity} / {total_h_capacity}"

        return result

    @staticmethod
    def system_split():
        pass
