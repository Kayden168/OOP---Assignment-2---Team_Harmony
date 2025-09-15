# Academic Integrity Statement
# filename: inventory.py
# author: Kayden Hong and Sandy
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 04 September 2025
# description: inventory class
# This is my own work as defined by the Academic Integrity Policy
from wire import Wire
from battery import Battery
from solarpanel import SolarPanel
from switch import Switch
from sensor import Sensor
from lightglobe import LightGlobe
from ledlight import LEDLight
from buzzer import Buzzer
from lightcircuit import LightCircuit
from sensorcircuit import SensorCircuit
from repository import Repository

class Inventory:
    def __init__(self):
        self.components = []
        self.circuits = []
        self.repo = Repository()

    def load_all(self):
        self.components = self.repo.load_components()
        self.circuits = self.repo.load_circuits()

    def save_all(self):
        self.repo.save_components(self.components)
        self.repo.save_circuits(self.circuits)

    def add_wire(self, length_mm, price, qty):
        i = 0
        while i < int(qty):
            self.components.append(Wire(int(length_mm), float(price)))
            i += 1
        self.repo.record_transaction("ADD_WIRE", str(length_mm) + "mm", qty, float(price) * int(qty))

    def add_battery(self, size, voltage, price, qty):
        i = 0
        while i < int(qty):
            self.components.append(Battery(str(size), float(voltage), float(price)))
            i += 1
        self.repo.record_transaction("ADD_BATTERY", str(size) + " " + str(voltage) + "V", qty, float(price) * int(qty))

    def add_solar_panel(self, voltage, current_ma, price, qty):
        i = 0
        while i < int(qty):
            self.components.append(SolarPanel(float(voltage), float(current_ma), float(price)))
            i += 1
        self.repo.record_transaction("ADD_SOLAR_PANEL", str(voltage) + "V " + str(current_ma) + "mA", qty, float(price) * int(qty))

    def add_switch(self, switch_type, voltage, price, qty):
        i = 0
        while i < int(qty):
            self.components.append(Switch(str(switch_type), float(voltage), float(price)))
            i += 1
        self.repo.record_transaction("ADD_SWITCH", str(switch_type) + " " + str(voltage) + "V", qty, float(price) * int(qty))

    def add_sensor(self, sensor_type, voltage, price, qty):
        i = 0
        while i < int(qty):
            self.components.append(Sensor(str(sensor_type), float(voltage), float(price)))
            i += 1
        self.repo.record_transaction("ADD_SENSOR", str(sensor_type) + " " + str(voltage) + "V", qty, float(price) * int(qty))

    def add_light_globe(self, color, voltage, current_ma, price, qty):
        i = 0
        while i < int(qty):
            self.components.append(LightGlobe(str(color), float(voltage), float(current_ma), float(price)))
            i += 1
        self.repo.record_transaction("ADD_LIGHT_GLOBE", str(color) + " " + str(voltage) + "V " + str(current_ma) + "mA", qty, float(price) * int(qty))

    def add_led_light(self, color, voltage, current_ma, price, qty):
        i = 0
        while i < int(qty):
            self.components.append(LEDLight(str(color), float(voltage), float(current_ma), float(price)))
            i += 1
        self.repo.record_transaction("ADD_LED_LIGHT", str(color) + " " + str(voltage) + "V " + str(current_ma) + "mA", qty, float(price) * int(qty))

    def add_buzzer(self, frequency_hz, sound_pressure_db, voltage, current_ma, price, qty):
        i = 0
        while i < int(qty):
            self.components.append(Buzzer(float(frequency_hz), float(sound_pressure_db), float(voltage), float(current_ma), float(price)))
            i += 1
        self.repo.record_transaction("ADD_BUZZER", str(frequency_hz) + "Hz " + str(int(float(sound_pressure_db))) + "dB " + str(voltage) + "V", qty, float(price) * int(qty))

    def create_light_circuit(self, name):
        c = LightCircuit(str(name))
        self.circuits.append(c)
        self.repo.record_transaction("NEW_LIGHT_CIRCUIT", str(name), 1, 0.0)
        return c

    def create_sensor_circuit(self, name):
        c = SensorCircuit(str(name))
        self.circuits.append(c)
        self.repo.record_transaction("NEW_SENSOR_CIRCUIT", str(name), 1, 0.0)
        return c

    def view_components(self):
        if len(self.components) == 0:
            print("No components")
            return
        i = 0
        while i < len(self.components):
            comp = self.components[i]
            print(str(i + 1) + ". " + comp.display_the_details())
            i += 1

    def view_circuits(self):
        if len(self.circuits) == 0:
            print("No circuits")
            return
        i = 0
        while i < len(self.circuits):
            cir = self.circuits[i]
            print(str(i + 1) + ". " + cir.display_the_details())
            i += 1

if __name__ == "__main__":
    inv = Inventory()
    inv.load_all()
    inv.view_components()
    inv.view_circuits()
