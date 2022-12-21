from abc import ABC, abstractmethod

class IComputer_Base(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

class Device(IComputer_Base):
   def __init__(self, cost):
       self.__cost = cost

   def cost(self) -> float:
       return self.__cost

class IDecorator(IComputer_Base):
    @abstractmethod
    def name(self) -> str:
        pass

class PC(IDecorator):

    def __init__(self, wrapped: IComputer_Base, pc_cost: float):
         self.__wrapped = wrapped
         self.__cost = pc_cost
         self.__name = "PC"

    def cost(self) -> float:
         return self.__cost + self.__wrapped.cost()

    def name(self) -> str:
         return self.__name

class Laptop(IDecorator):

    def __init__(self, wrapped: IComputer_Base, laptop_cost: float):
        self.__wrapped = wrapped
        self.__cost = laptop_cost
        self.__name = "Laptop"

    def cost(self) -> float:
            return (self.__cost + self.__wrapped.cost())

    def name(self) -> str:
            return self.__name

if __name__ == "__main__":
     def print_device(device: IDecorator) -> None:
         print(f"Стоимость устройства '{device.name()}' = {device.cost()} ")

     device_base = Device(1000)
     print(f"Цена упаковки = {device_base.cost()}")
     PC = PC(device_base, 69000)
     print_device(PC)
     Laptop = Laptop(device_base, 59000)
     print_device(Laptop)