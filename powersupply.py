# File: powersupply.py
# Author: sandhya thapaliya
# ID: 522895
# Email: 522895@learning.eynesbury.edu.au
# Description: Abstract PowerSupply base class
# This is my own work as defined by the Academic Integrity Policy

from abc import ABC
from component import Component

class PowerSupply(Component, ABC):
    def __init__(self, name: str, price: float, voltage: float) -> None:
        super().__init__(name, price)
        self.__voltage = float(voltage)

    @property
    def voltage(self) -> float:
        return self.__voltage

    @voltage.setter
    def voltage(self, value: float) -> None:
        self.__voltage = float(value)
