from unittest import TestCase, main
from car_manager import Car

class TestCar(TestCase):
    
    def setUp(self):
        self.car = Car("Nissan", "GT-R", 15, 75)
        
        
    def test_correct_init(self):
        self.assertEqual("Nissan", self.car.make)    
        self.assertEqual("GT-R", self.car.model)    
        self.assertEqual(15, self.car.fuel_consumption)    
        self.assertEqual(75, self.car.fuel_capacity)    
        self.assertEqual(0, self.car.fuel_amount)    


    



if __name__ == "__main__":
    main()