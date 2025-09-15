#Academic Integrity Statement
# filename: repository.py
# author: sandhya thapaliya
# student ID: 522895
# email: 522895@learning.eynesbury.edu.au
# date: 15 September 2025
# description: repository class
# This is my own work as defined by the Academic Integrity Policy
import csv
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

class Repository:
    def __init__(self, components_csv="components.csv", circuits_csv="circuits.csv", transactions_csv="transactions.csv"):
        self.components_csv = components_csv
        self.circuits_csv = circuits_csv
        self.transactions_csv = transactions_csv

    def save_components(self, components):
        lines = []
        i = 0
        while i < len(components):
            lines.append(components[i].to_csv_str())
            i += 1
        self._write_lines(self.components_csv, lines)

    def save_circuits(self, circuits):
        lines = []
        i = 0
        while i < len(circuits):
            lines.append(circuits[i].to_csv_str())
            i += 1
        self._write_lines(self.circuits_csv, lines)

    def load_components(self):
        result = []
        try:
            lines = self._read_lines(self.components_csv)
        except FileNotFoundError:
            return result
        i = 0
        while i < len(lines):
            line = lines[i]
            parts = line.split(",")
            if len(parts) > 0:
                t = parts[0].strip().lower()
                if t == "wire" and len(parts) >= 3:
                    result.append(Wire(int(parts[1]), float(parts[2])))
                elif t == "battery" and len(parts) >= 4:
                    result.append(Battery(parts[1], float(parts[2]), float(parts[3])))
                elif t == "solar panel" and len(parts) >= 4:
                    result.append(SolarPanel(float(parts[1]), float(parts[2]), float(parts[3])))
                elif t == "switch" and len(parts) >= 4:
                    result.append(Switch(parts[1], float(parts[2]), float(parts[3])))
                elif t == "sensor" and len(parts) >= 4:
                    result.append(Sensor(parts[1], float(parts[2]), float(parts[3])))
                elif t == "light globe" and len(parts) >= 5:
                    result.append(LightGlobe(parts[1], float(parts[2]), float(parts[3]), float(parts[4])))
                elif t == "led light" and len(parts) >= 5:
                    result.append(LEDLight(parts[1], float(parts[2]), float(parts[3]), float(parts[4])))
                elif t == "buzzer" and len(parts) >= 6:
                    result.append(Buzzer(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5])))
            i += 1
        return result

    def load_circuits(self):
        result = []
        try:
            lines = self._read_lines(self.circuits_csv)
        except FileNotFoundError:
            return result
        i = 0
        while i < len(lines):
            line = lines[i]
            parts = line.split(",")
            if len(parts) > 0:
                t = parts[0].strip().lower()
                if t == "lightcircuit" and len(parts) >= 2:
                    result.append(LightCircuit(parts[1]))
                elif t == "sensorcircuit" and len(parts) >= 2:
                    result.append(SensorCircuit(parts[1]))
            i += 1
        return result

    def record_transaction(self, action, item, qty, amount):
        try:
            f = open(self.transactions_csv, mode="a", newline="", encoding="utf-8")
            w = csv.writer(f)
            w.writerow([str(action), str(item), int(qty), str(float(amount))])
            f.close()
        except:
            pass

    def _write_lines(self, path, lines):
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
