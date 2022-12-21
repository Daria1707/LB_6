from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import List

class DeviceType(Enum):
    PC = 1
    Laptop = 2
    Tablet = 3

class Device:
    device_id: int = 1

    def __init__(self, device_type: DeviceType):
        self.id = Device.device_id
        self.type = device_type
        Device.device_id += 1

    def __str__(self):
        return f"устройство {self.type.name} (Заказ №{self.id}) "

class Observer(ABC):
    @abstractmethod
    def update(self, order_id: int):
        ...

class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, order_id: int) -> None:
        for observer in self._observers:
            observer.update(order_id)

class Devices(Subject):
   def __init__(self):
       super().__init__()
       self.__device: List[Device] = []
       self.__finish_device: List[Device] = []

   def take_device(self, device:Device) -> None:
       print(f"Было куплено {device}")
       self.__device.append(device)

   def get_device(self, device_id: int) -> Device:
       device = None
       for it in self.__finish_device:
           if it.id == device_id:
              device = it
              break
       self.__finish_device.remove(device)
       return device

class Client(Observer):
    def __init__(self, name: str, administrator: Device):
        self.__administrator = administrator
        self.__name = name
        self.device: Device = None

    def update(self, device_id: int) -> None:
        if self.device is not None:
           if device_id == self.device.id:
              self.__administrator.detach(self)

    def create_order(self) -> None:
        device_type = choice([DeviceType.PC,
                             DeviceType.Laptop,
                             DeviceType.Tablet])
        self.device = Device(device_type)
        print(f"Клиент {self.__name} выбрал {self.device}")
        self.__administrator.attach(self)
        self.__administrator.take_device(self.device)

if __name__ == "__main__":
     names = ['Марьяна', 'Дарья',
              'Светлана', 'Дмитрий']
     Organization = Devices()
     clients = [Client(name, Organization) for name in names]
     for client in clients:
         print("*"*50)
         client.create_order()