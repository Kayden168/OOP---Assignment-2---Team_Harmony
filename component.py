# File: component.py
# Author: sandhya thapaliya
# ID: 522895
# Email: 522895@learning.eynesbury.edu.au
# Description: Component hierarchy for electronics inventory app
# This is my own work as defined by the Academic Integrity Policy
from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, name: str, price: float) -> None:
        self.__name = name
        self.__price = float(price)

    @property
    def name(self) -> str:
        return self.__name