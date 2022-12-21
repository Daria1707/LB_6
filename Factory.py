from enum import Enum

class NameDevice(Enum):
    PC = 0,
    Laptop = 1,
    Tablet = 2,

class Device:

    def __init__(self, price: float):
        self.__price = price

    def get_price(self) -> float:
        return self.__price


class Device_PC(Device):
    def __init__(self):
        super().__init__(60000)

class Device_Laptop(Device):
    def __init__(self):
        super().__init__(50000)

class Device_Tablet(Device):
    def __init__(self):
        super().__init__(30000)

def SaleDevice(device_type: NameDevice) -> Device:
    factory_dict = {
        NameDevice.PC: Device_PC,
        NameDevice.Laptop: Device_Laptop,
        NameDevice.Tablet: Device_Tablet,
    }
    return factory_dict[device_type]()

if __name__ == '__main__':
    for Device in NameDevice:
        device = SaleDevice(Device)
        print(f' Тип устройства: {Device}, цена: {device.get_price()}')