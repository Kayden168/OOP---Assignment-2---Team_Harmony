import unittest
from app import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_add_wire_and_battery(self):
        start = len(self.app.inventory.components)
        self.app.inventory.add_wire(100, 2.5, 2)
        self.app.inventory.add_battery("AA", 1.5, 0.9, 3)
        end = len(self.app.inventory.components)
        self.assertEqual(end, start + 5)

    def test_create_circuits(self):
        start = len(self.app.inventory.circuits)
        self.app.inventory.create_light_circuit("LC1")
        self.app.inventory.create_sensor_circuit("SC1")
        end = len(self.app.inventory.circuits)
        self.assertEqual(end, start + 2)

if __name__ == "__main__":
    unittest.main()
