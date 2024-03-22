import unittest

class SimpleTest(unittest.TestCase):
    def test_upper(self):
        result = 'foo'.upper()
        expected_result = 'FOO'
        self.assertEqual(result, expected_result)
        

# Running the test        
if __name__ == '__main__':
    unittest.main()        