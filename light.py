# Academic Integrity Statement
# filename: light.py
# author: Kayden Hong
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 04 September 2025
# description: light class
# This is my own work as defined by the Academic Integrity Policy
from abc import ABC
from outputcomponent import OutputComponent

class Light(OutputComponent, ABC):
    def __init__(self, name: str, price: float, color: str, voltage: float, current_ma: float) -> None:
        super().__init__(name, price)
        self.__color = color
        self.__voltage = float(voltage)
        self.__current_ma = float(current_ma)
        return
    
    @property
    def color(self) -> str:
        return self.__color
    
    @color.setter
    def color(self, value: str) -> None:
        self.__color =  value
        return
    
    @property
    def voltage(self) -> float:
        return self.__voltage
    
    @voltage.setter
    def voltage(self, value: float) -> None:
        self.__voltage = float(value)
        return
    
    @property
    def current_ma(self) -> float:
        return self.__current_ma
    
    @current_ma.setter
    def current_ma(self, value: float) -> None:
        self.__current_ma = float(value)
        return
    pass