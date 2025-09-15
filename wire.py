# Academic Integrity Statement
# filename: wire.py
# author: Kayden Hong
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 04 September 2025
# description: wire class
# This is my own work as defined by the Academic Integrity Policy
from component import Component

class Wire(Component):
    def __init__(self, length_mm: int, price: float) -> None:
        super().__init__("Wire", price)
        self.__length_mm = int(length_mm)

    @property
    def length_mm(self) -> int:
        return self.__length_mm

    @length_mm.setter
    def length_mm(self, value: int) -> None:
        self.__length_mm = int(value)

    def to_csv_str(self) -> str:
        return f"Wire,{self.length_mm},{self.price:.2f}"

    def duplicate(self):
        return Wire(self.length_mm, self.price)

    def display_the_details(self) -> str:
        return f"{self.length_mm}mm Wire ${self.price:.2f}"

    @classmethod
    def parse_csv(cls, csv_str: str):
        pass