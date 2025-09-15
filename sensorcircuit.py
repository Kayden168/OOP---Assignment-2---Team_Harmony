#Academic Integrity Statement
# filename: sensorcircuit.py
# author: sandhya thapaliya
# student ID: 522895
# email: 522895@learning.eynesbury.edu.au
# date: 15 September 2025
# description: outputcomponent class
# This is my own work as defined by the Academic Integrity Policy
from circuit import Circuit
from sensor import Sensor

class SensorCircuit(Circuit):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def to_csv_str(self) -> str:
        return "SensorCircuit," + self.name + "," + str(len(self.components))

    def duplicate(self):
        copy = SensorCircuit(self.name)
        for c in self.components:
            if isinstance(c, Sensor):
                copy.add_component(c.duplicate())
        return copy

    def display_the_details(self) -> str:
        details = "Sensor Circuit: " + self.name + "\n"
        if len(self.components) == 0:
            details += "No components.\n"
        else:
            for c in self.components:
                details += "- " + c.display_the_details() + "\n"
        return details

    @classmethod
    def parse_csv(cls, csv_str: str):
        pass
