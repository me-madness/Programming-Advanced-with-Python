from unittest import TestCase, main

class SimpleTest(unittest.TestCase):
    
    def test_upper(self):
        result = 'foo'.upper()
        expected_result = 'FOO'
        self.assertEqual(result, expected_result)
        

class MyCar:
    
    def __init__(self, model: str, hp: int) -> None:
        self.model = model
        self.hp = hp



# Running the test        
if __name__ == '__main__':
    unittest.main()        