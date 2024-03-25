from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    
    def setUp(self):
        self.vehicle = Vehicle(100, 100)
        
    
    def test_default_fuel_consumption_is_correct_value(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)
    
        
    def test_correct_init(self):    
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)
    
    
    def test_drive_without_fuel_raises_exception(self):
        
        
        
        
        
if __name__ == "__main__":
    main()        