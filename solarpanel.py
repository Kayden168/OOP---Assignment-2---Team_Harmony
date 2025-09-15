# Academic Integrity Statement
# filename: solarpanel.py
# author: Kayden Hong
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 04 September 2025
# description: solarpanel class
# This is my own work as defined by the Academic Integrity Policy
from powersupply import PowerSupply

class SolarPanel(PowerSupply):
    def __init__(self, voltage: float, current_ma: float, price: float) -> None:
        super().__init__("Solar Panel", price, voltage)
        self.__current_ma = float(current_ma)

    @property
    def current_ma(self) -> float:
        return self.__current_ma

    @current_ma.setter
    def current_ma(self, value: float) -> None:
        self.__current_ma = float(value)

    def to_csv_str(self) -> str:
        return f"Solar Panel,{self.voltage:.1f},{self.current_ma:.1f},{self.price:.2f}"

    def duplicate(self):
        return SolarPanel(self.voltage, self.current_ma, self.price)

    def display_the_details(self) -> str:
        return f"{self.voltage:.1f}V {self.current_ma:.1f}mA Solar Panel ${self.price:.2f}"

    @classmethod
    def parse_csv(cls, csv_str: str):
        pass
