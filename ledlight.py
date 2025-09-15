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
