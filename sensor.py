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
