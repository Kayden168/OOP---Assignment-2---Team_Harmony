#Academic Integrity Statement
# filename: switch.py
# author: sandhya thapaliya
# student ID: 522895
# email: 522895@learning.eynesbury.edu.au
# date: 15 September 2025
# description: switch class
# This is my own work as defined by the Academic Integrity Policy
from inputcomponent import InputComponent

class Switch(InputComponent):
    def __init__(self, switch_type: str, voltage: float, price: float) -> None:
        super().__init__("Switch", price)
        self.__switch_type = switch_type.lower()
        self.__voltage = float(voltage)

    @property
    def switch_type(self) -> str:
        return self.__switch_type

    @switch_type.setter
    def switch_type(self, value: str) -> None:
        self.__switch_type = value.lower()
        

    @property
    def voltage(self) -> float:
        return self.__voltage

    @voltage.setter
    def voltage(self, value: float) -> None:
        self.__voltage = float(value)

    def to_csv_str(self) -> str:
        return "Switch," + self.switch_type + "," + "{:.1f}".format(self.voltage) + "," + "{:.2f}".format(self.price)

    def duplicate(self):
        return Switch(self.switch_type, self.voltage, self.price)

    def display_the_details(self) -> str:
        t = self.switch_type.capitalize()
        return "{:.1f}".format(self.voltage) + "V " + t + " Switch $" + "{:.2f}".format(self.price)
    
    @classmethod
    def parse_csv(cls, csv_str: str):
        pass
