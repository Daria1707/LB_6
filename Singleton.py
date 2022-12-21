class Computer_Base(type):
   _instances = {}
   def __call__(cls, *args, **kwargs):
       if cls not in cls._instances:
           cls._instances[cls] = super(Computer_Base, cls).\
               __call__(*args, **kwargs)
       return cls._instances[cls]

class Device(metaclass = Computer_Base):
    def __init__(self):
        self.name = "PC"

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

if __name__ == "__main__":
    PC = Device()
    Laptop = Device()
    Tablet = Device()
    print("Name_First_Device: " + PC.get_name())
    PC.set_name("Laptop")
    print("Name_Second_Device: " + Laptop.get_name())
    Laptop.set_name("Tablet")
    print("Name_Third_Device: " + Tablet.get_name())
    print(PC)
    print(Laptop)
    print(Tablet)
    print(id(PC) == id(Laptop) == id(Tablet))
