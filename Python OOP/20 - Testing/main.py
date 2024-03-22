from unittest import TestCase, main
import unittest
class SimpleTest(unittest.TestCase):
    
    def test_upper(self):
        result = 'foo'.upper()
        expected_result = 'FOO'
        self.assertEqual(result, expected_result)
        

class MyCar:
    
    def __init__(self, model: str, hp: int) -> None:
        self.model = model
        self.hp = hp


class TestMyCar(TestCase):
    
    def test_correct_init(self):
        model, hp = "BMW", 100
        
        my_car = MyCar(model, hp)
        
        self.assertEqual(my_car.model, model)
        self.assertEqual(my_car.hp, hp)


# Running the test        
if __name__ == '__main__':
    unittest.main()        