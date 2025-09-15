from light import Light

class LightGlobe(Light):
    def __init__(self, color: str, voltage: float, current_ma: float, price: float) -> None:
        super().__init__("Light Globe", price, color, voltage, current_ma)

    def to_csv_str(self) -> str:
        return "Light Globe," + self.color + "," + "{:.1f}".format(self.voltage) + "," + "{:.1f}".format(self.current_ma) + "," + "{:.2f}".format(self.price)

    def duplicate(self):
        return LightGlobe(self.color, self.voltage, self.current_ma, self.price)