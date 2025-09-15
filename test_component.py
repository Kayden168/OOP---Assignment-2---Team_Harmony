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

if __name__ == "__main__":
    unittest.main()
