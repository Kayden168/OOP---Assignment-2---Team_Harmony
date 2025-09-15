#Academic Integrity Statement
# filename: test_component.py
# author: sandhya thapaliya
# student ID: 522895
# email: 522895@learning.eynesbury.edu.au
# date: 15 September 2025
# description: test_component class
# This is my own work as defined by the Academic Integrity Policy
import unittest
from wire import Wire
from battery import Battery
from solarpanel import SolarPanel
from switch import Switch
from sensor import Sensor
from lightglobe import LightGlobe
from ledlight import LEDLight
from buzzer import Buzzer

class TestWire(unittest.TestCase):
    def test_duplicate(self):
        w1 = Wire(100, 2.5)
        w2 = w1.duplicate()
        self.assertEqual(w1.length_mm, w2.length_mm)
        self.assertEqual(w1.price, w2.price)
        self.assertIsNot(w1, w2)

    def test_to_csv_str(self):
        w = Wire(150, 3.0)
        self.assertEqual(w.to_csv_str(), "Wire,150,3.00")
        pass

class TestBattery(unittest.TestCase):
    def test_duplicate(self):
        b1 = Battery("AA", 1.5, 0.9)
        b2 = b1.duplicate()
        self.assertEqual(b1.size, b2.size)
        self.assertEqual(b1.voltage, b2.voltage)
        self.assertEqual(b1.price, b2.price)
        self.assertIsNot(b1, b2)

    def test_to_csv_str(self):
        b = Battery("AA", 1.5, 0.9)
        self.assertEqual(b.to_csv_str(), "Battery,AA,1.5,0.90")
        pass

class TestSolarPanel(unittest.TestCase):
    def test_to_csv_str(self):
        sp = SolarPanel(5.0, 200.0, 10.0)
        self.assertEqual(sp.to_csv_str(), "Solar Panel,5.0,200.0,10.00")
        pass

class TestSwitch(unittest.TestCase):
    def test_to_csv_str(self):
        s = Switch("toggle", 3.3, 1.2)
        self.assertEqual(s.to_csv_str(), "Switch,toggle,3.3,1.20")
        pass

class TestSensor(unittest.TestCase):
    def test_to_csv_str(self):
        s = Sensor("temperature", 5.0, 2.5)
        self.assertEqual(s.to_csv_str(), "Sensor,temperature,5.0,2.50")
        pass

class TestLightGlobe(unittest.TestCase):
    def test_to_csv_str(self):
        lg = LightGlobe("red", 3.0, 20.0, 1.5)
        self.assertEqual(lg.to_csv_str(), "Light Globe,red,3.0,20.0,1.50")
        pass

class TestLEDLight(unittest.TestCase):
    def test_to_csv_str(self):
        led = LEDLight("green", 3.0, 15.0, 2.0)
        self.assertEqual(led.to_csv_str(), "LED Light,green,3.0,15.0,2.00")
        pass

class TestBuzzer(unittest.TestCase):
    def test_to_csv_str(self):
        bz = Buzzer(4000.0, 85.0, 5.0, 30.0, 1.2)
        self.assertEqual(bz.to_csv_str(), "Buzzer,4000.0,85,5.0,30.0,1.20")
        pass

if __name__ == "__main__":
    unittest.main()
