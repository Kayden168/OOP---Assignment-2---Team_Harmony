# Academic Integrity Statement
# filename: app.py
# author: Kayden Hong Sandy
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 15 September 2025
# description: app class
# This is my own work as defined by the Academic Integrity Policy
import csv
from component import Component
from wire import Wire
from battery import Battery
from solarpanel import SolarPanel
from switch import Switch
from sensor import Sensor
from lightglobe import LightGlobe
from ledlight import LEDLight
from buzzer import Buzzer
from circuit import Circuit
from lightcircuit import LightCircuit
from sensorcircuit import SensorCircuit

class App:
    def __init__(self) -> None:
        self.components = []
        self.circuits = []
        self.components_csv = "components.csv"
        self.circuits_csv = "circuits.csv"
        self.transactions_csv = "transactions.csv"

    def add_wire(self, length_mm, price, qty) -> None:
        i = 0
        while i < int(qty):
            self.components.append(Wire(int(length_mm), float(price)))
            i += 1
        self.record_transaction("ADD_WIRE", str(qty), qty, float(price) * int(qty))

    def add_battery(self, size, voltage, price, qty) -> None:
        i = 0
        while i < int(qty):
            self.components.append(Battery(str(size), float(voltage), float(price)))
            i += 1
        self.record_transaction("ADD_BATTERY", str(size) + " " + str(voltage) + "V", qty, float(price) * int(qty))

    def add_solar_panel(self, voltage, current_ma, price, qty) -> None:
        i = 0
        while i < int(qty):
            self.components.append(SolarPanel(float(voltage), float(current_ma), float(price)))
            i += 1
        self.record_transaction("ADD_SOLAR_PANEL", str(voltage) + "V " + str(current_ma) + "mA", qty, float(price) * int(qty))

    def add_switch(self, switch_type, voltage, price, qty) -> None:
        i = 0
        while i < int(qty):
            self.components.append(Switch(str(switch_type), float(voltage), float(price)))
            i += 1
        self.record_transaction("ADD_SWITCH", str(switch_type) + " " + str(voltage) + "V", qty, float(price) * int(qty))

    def add_sensor(self, sensor_type, voltage, price, qty) -> None:
        i = 0
        while i < int(qty):
            self.components.append(Sensor(str(sensor_type), float(voltage), float(price)))
            i += 1
        self.record_transaction("ADD_SENSOR", str(sensor_type) + " " + str(voltage) + "V", qty, float(price) * int(qty))

    def add_light_globe(self, color, voltage, current_ma, price, qty) -> None:
        i = 0
        while i < int(qty):
            self.components.append(LightGlobe(str(color), float(voltage), float(current_ma), float(price)))
            i += 1
        self.record_transaction("ADD_LIGHT_GLOBE", str(color) + " " + str(voltage) + "V " + str(current_ma) + "mA", qty, float(price) * int(qty))

    def add_led_light(self, color, voltage, current_ma, price, qty) -> None:
        i = 0
        while i < int(qty):
            self.components.append(LEDLight(str(color), float(voltage), float(current_ma), float(price)))
            i += 1
        self.record_transaction("ADD_LED_LIGHT", str(color) + " " + str(voltage) + "V " + str(current_ma) + "mA", qty, float(price) * int(qty))

    def add_buzzer(self, frequency_hz, sound_pressure_db, voltage, current_ma, price, qty) -> None:
        i = 0
        while i < int(qty):
            self.components.append(Buzzer(float(frequency_hz), float(sound_pressure_db), float(voltage), float(current_ma), float(price)))
            i += 1
        self.record_transaction("ADD_BUZZER", str(frequency_hz) + "Hz " + str(int(float(sound_pressure_db))) + "dB " + str(voltage) + "V", qty, float(price) * int(qty))

    def create_light_circuit(self, name) -> LightCircuit:
        c = LightCircuit(str(name))
        self.circuits.append(c)
        self.record_transaction("NEW_LIGHT_CIRCUIT", str(name), 1, 0.0)
        return c

    def create_sensor_circuit(self, name) -> SensorCircuit:
        c = SensorCircuit(str(name))
        self.circuits.append(c)
        self.record_transaction("NEW_SENSOR_CIRCUIT", str(name), 1, 0.0)
        return c

    def view_components(self) -> None:
        if len(self.components) == 0:
            print("No components")
            return
        i = 0
        while i < len(self.components):
            comp = self.components[i]
            print(str(i + 1) + ". " + comp.display_the_details())
            i += 1

    def view_circuits(self) -> None:
        if len(self.circuits) == 0:
            print("No circuits")
            return
        i = 0
        while i < len(self.circuits):
            cir = self.circuits[i]
            print(str(i + 1) + ". " + cir.display_the_details())
            i += 1

    def save_components(self) -> None:
        lines = []
        i = 0
        while i < len(self.components):
            lines.append(self.components[i].to_csv_str())
            i += 1
        self._write_lines(self.components_csv, lines)

    def save_circuits(self) -> None:
        lines = []
        i = 0
        while i < len(self.circuits):
            lines.append(self.circuits[i].to_csv_str())
            i += 1
        self._write_lines(self.circuits_csv, lines)

    def load_components(self) -> None:
        try:
            lines = self._read_lines(self.components_csv)
        except FileNotFoundError:
            return
        i = 0
        while i < len(lines):
            line = lines[i]
            parts = line.split(",")
            if len(parts) > 0:
                t = parts[0].strip().lower()
                if t == "wire" and len(parts) >= 3:
                    obj = Wire(int(parts[1]), float(parts[2]))
                    self.components.append(obj)
                elif t == "battery" and len(parts) >= 4:
                    obj = Battery(parts[1], float(parts[2]), float(parts[3]))
                    self.components.append(obj)
                elif t == "solar panel" and len(parts) >= 4:
                    obj = SolarPanel(float(parts[1]), float(parts[2]), float(parts[3]))
                    self.components.append(obj)
                elif t == "switch" and len(parts) >= 4:
                    obj = Switch(parts[1], float(parts[2]), float(parts[3]))
                    self.components.append(obj)
                elif t == "sensor" and len(parts) >= 4:
                    obj = Sensor(parts[1], float(parts[2]), float(parts[3]))
                    self.components.append(obj)
                elif t == "light globe" and len(parts) >= 5:
                    obj = LightGlobe(parts[1], float(parts[2]), float(parts[3]), float(parts[4]))
                    self.components.append(obj)
                elif t == "led light" and len(parts) >= 5:
                    obj = LEDLight(parts[1], float(parts[2]), float(parts[3]), float(parts[4]))
                    self.components.append(obj)
                elif t == "buzzer" and len(parts) >= 6:
                    obj = Buzzer(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5]))
                    self.components.append(obj)
            i += 1

    def load_circuits(self) -> None:
        try:
            lines = self._read_lines(self.circuits_csv)
        except FileNotFoundError:
            return
        i = 0
        while i < len(lines):
            line = lines[i]
            parts = line.split(",")
            if len(parts) > 0:
                t = parts[0].strip().lower()
                if t == "lightcircuit" and len(parts) >= 2:
                    self.circuits.append(LightCircuit(parts[1]))
                elif t == "sensorcircuit" and len(parts) >= 2:
                    self.circuits.append(SensorCircuit(parts[1]))
            i += 1

    def record_transaction(self, action, item, qty, amount) -> None:
        try:
            f = open(self.transactions_csv, mode="a", newline="", encoding="utf-8")
            w = csv.writer(f)
            w.writerow([str(action), str(item), int(qty), str(float(amount))])
            f.close()
        except:
            pass

    def _write_lines(self, path, lines) -> None:
        f = open(path, "w", encoding="utf-8")
        i = 0
        while i < len(lines):
            f.write(lines[i] + "\n")
            i += 1
        f.close()

    def _read_lines(self, path):
        f = open(path, "r", encoding="utf-8")
        data = f.read().splitlines()
        f.close()
        return data

if __name__ == "__main__":
    app = App()
    try:
        app.load_components()
        app.load_circuits()
    except:
        pass
    app.view_components()
    app.view_circuits()