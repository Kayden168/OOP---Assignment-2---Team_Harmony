# Academic Integrity Statement
# filename: test_circuit.py
# author: Kayden Hong
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 04 September 2025
# description: test_circuit class
# This is my own work as defined by the Academic Integrity Policy
import unittest
from lightcircuit import LightCircuit
from lightglobe import LightGlobe

class TestLightCircuit(unittest.TestCase):
    def test_add_and_duplicate(self):
        c1 = LightCircuit("Test")
        lg = LightGlobe("red", 3.0, 20.0, 1.5)
        c1.add_component(lg)
        c2 = c1.duplicate()
        self.assertEqual(len(c1.components), len(c2.components))
        self.assertIsNot(c1.components[0], c2.components[0])

if __name__ == "__main__":
    unittest.main()