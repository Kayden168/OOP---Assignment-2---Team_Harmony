# File: battery.py
# Author: sandhya thapaliya
# ID: 522895
# Email: 522895@learning.eynesbury.edu.au
# Description: Component hierarchy for electronics inventory app
# This is my own work as defined by the Academic Integrity Policy
from powersupply import PowerSupply

class Battery(PowerSupply):
    def __init__(self, size: str, voltage: float, price: float) -> None:
        super().__init__("Battery", price, voltage)
        self.__size = size.upper()

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, value: str) -> None:
        self.__size = value.upper()

    def to_csv_str(self) -> str:
        return "Battery," + self.size + "," + "{:.1f}".format(self.voltage) + "," + "{:.2f}".format(self.price)

    def duplicate(self):
        return Battery(self.size, self.voltage, self.price)

    def display_the_details(self) -> str:
        return "{:.1f}".format(self.voltage) + "V " + self.size + " Battery $" + "{:.2f}".format(self.price)

    @classmethod
    def parse_csv(cls, csv_str: str):
        pass