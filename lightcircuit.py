# Academic Integrity Statement
# filename: lightcircuit.py
# author: Kayden Hong
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 04 September 2025
# description: lightcircuit class
# This is my own work as defined by the Academic Integrity Policy
from circuit import Circuit
from light import Light

class LightCircuit(Circuit):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def to_csv_str(self) -> str:
        return "LightCircuit," + self.name + "," + str(len(self.components))

    def duplicate(self):
        copy = LightCircuit(self.name)
        for c in self.components:
            if isinstance(c, Light):
                copy.add_component(c.duplicate())
        return copy

    def display_the_details(self) -> str:
        details = "Light Circuit: " + self.name + "\n"
        if len(self.components) == 0:
            details += "No components.\n"
        else:
            for c in self.components:
                details += "- " + c.display_the_details() + "\n"
        return details

    @classmethod
    def parse_csv(cls, csv_str: str):
        pass