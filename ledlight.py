# Academic Integrity Statement
# filename: lightcircuit.py
# author: sandhya thapaliya
# student ID: 522895
# email: 522895@learning.eynesbury.edu.au
# date: 04 September 2025
# description: ledlight class
# This is my own work as defined by the Academic Integrity Policy
from light import Light

class LEDLight(Light):
    def __init__(self, color: str, voltage: float, current_ma: float, price: float) -> None:
        super().__init__("LED Light", price, color, voltage, current_ma)

    def to_csv_str(self) -> str:
        return "LED Light," + self.color + "," + "{:.1f}".format(self.voltage) + "," + "{:.1f}".format(self.current_ma) + "," + "{:.2f}".format(self.price)

    def duplicate(self):
        return LEDLight(self.color, self.voltage, self.current_ma, self.price)

    def display_the_details(self) -> str:
        c = self.color.capitalize()
        return "{:.1f}".format(self.voltage) + "V " + "{:.1f}".format(self.current_ma) + "mA " + c + " LED Light $" + "{:.2f}".format(self.price)

    @classmethod
    def parse_csv(cls, csv_str: str):
        pass
