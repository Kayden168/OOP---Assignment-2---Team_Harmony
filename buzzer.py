# Academic Integrity Statement
# filename: buzzer.py
# author: Kayden Hong
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 04 September 2025
# description: buzzer class
# This is my own work as defined by the Academic Integrity Policy

from outputcomponent import OutputComponent

class Buzzer(OutputComponent):
    def __init__(self, frequency_hz: float, sound_pressure_db: float, voltage: float, current_ma: float, price: float) -> None:
        super().__init__("Buzzer", price)
        self.__frequency_hz = float(frequency_hz)
        self.__sound_pressure_db = float(sound_pressure_db)
        self.__voltage = float(voltage)
        self.__current_ma = float(current_ma)

    @property
    def frequency_hz(self) -> float:
        return self.__frequency_hz

    @frequency_hz.setter
    def frequency_hz(self, value: float) -> None:
        self.__frequency_hz = float(value)

    @property
    def sound_pressure_db(self) -> float:
        return self.__sound_pressure_db

    @sound_pressure_db.setter
    def sound_pressure_db(self, value: float) -> None:
        self.__sound_pressure_db = float(value)

    @property
    def voltage(self) -> float:
        return self.__voltage

    @voltage.setter
    def voltage(self, value: float) -> None:
        self.__voltage = float(value)

    @property
    def current_ma(self) -> float:
        return self.__current_ma

    @current_ma.setter
    def current_ma(self, value: float) -> None:
        self.__current_ma = float(value)

    def to_csv_str(self) -> str:
        return "Buzzer," + "{:.1f}".format(self.frequency_hz) + "," + "{:.0f}".format(self.sound_pressure_db) + "," + "{:.1f}".format(self.voltage) + "," + "{:.1f}".format(self.current_ma) + "," + "{:.2f}".format(self.price)

    def duplicate(self):
        return Buzzer(self.frequency_hz, self.sound_pressure_db, self.voltage, self.current_ma, self.price)

    def display_the_details(self) -> str:
        return "{:.1f}".format(self.voltage) + "V " + "{:.1f}".format(self.current_ma) + "mA " + "{:.1f}".format(self.frequency_hz) + "Hz " + str(int(self.sound_pressure_db)) + "dB Buzzer $" + "{:.2f}".format(self.price)

    @classmethod
    def parse_csv(cls, csv_str: str):
        pass