# Academic Integrity Statement
# filename: circuit.py
# author: Kayden Hong
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 04 September 2025
# description: circuit class
# This is my own work as defined by the Academic Integrity Policy
from abc import ABC, abstractmethod
from component import Component

class Circuit(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__components = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def components(self):
        return self.__components

    def add_component(self, component: Component) -> None:
        self.__components.append(component)

    def remove_component(self, component: Component) -> None:
        if component in self.__components:
            self.__components.remove(component)

    @abstractmethod
    def to_csv_str(self) -> str:
        pass

    @abstractmethod
    def duplicate(self):
        pass

    @abstractmethod
    def display_the_details(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def parse_csv(cls, csv_str: str):
        pass