#Academic Integrity Statement
# filename: sensor.py
# author: sandhya thapaliya
# student ID: 522895
# email: 522895@learning.eynesbury.edu.au
# date: 15 September 2025
# description: outputcomponent class
# This is my own work as defined by the Academic Integrity Policy
from inputcomponent import InputComponent

class Sensor(InputComponent):
    def __init__(self, sensor_type: str, voltage: float, price: float) -> None:
        super().__init__("Sensor", price)
        self.__sensor_type = sensor_type.lower()
        self.__voltage = float(voltage)

    @property
    def sensor_type(self) -> str:
        return self.__sensor_type

    @sensor_type.setter
    def sensor_type(self, value: str) -> None:
        self.__sensor_type = value.lower()

    @property
    def voltage(self) -> float:
        return self.__voltage
    
    @voltage.setter
    def voltage(self, value: float) -> None:
        self.__voltage = float(value)

    def to_csv_str(self) -> str:
        return "Sensor," + self.sensor_type + "," + "{:.1f}".format(self.voltage) + "," + "{:.2f}".format(self.price)

    def duplicate(self):
        return Sensor(self.sensor_type, self.voltage, self.price)

    def display_the_details(self) -> str:
        t = self.sensor_type.capitalize()
        return "{:.1f}".format(self.voltage) + "V " + t + " Sensor $" + "{:.2f}".format(self.price)

    @classmethod
    def parse_csv(cls, csv_str: str):
        pass