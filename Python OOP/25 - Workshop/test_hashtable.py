from unittest import TestCase, main
from hashtable import HashTable

class TestHashTable(TestCase):
    
    def setUp(self):
        self.h = HashTable()
    
    
    def test_init(self):
        self.assertEqual(self.h._HashTable__keys, [None, None, None, None])
        self.assertEqual(self.h._HashTable__values, [None, None, None, None])
        self.assertEqual(self.h._HashTable__length, 4)
    
    
    def test_count(self):
        result = self.h.count
        self.assertEqual(result, 0)
        
        # TODO test when there is element which is not None
        
        
    def test_length(self):
        self.assertEqual(len(self.h), 4)    
        self.assertEqual(len(self.h), self.h._HashTable__length)    
    
        # Test with resizing
        self.h["name"] = "Peter"
        self.h["age"] = 25
        self.h["id"] = 1
        self.h["city"] = "Sofiq"
        self.h["street"] = "Markovo Tepe"
        self.h["name"] = "Test"
        self.h["city"] = "Plovdiv"
    
        self.assertEqual(len(self.h), 8)    
        self.assertEqual(len(self.h), self.h._HashTable__length)
    
    
    def test_get_item(self):
        self.h["name"] = "Peter"
    
        self.assertEqual(self.h["name"], "Peter")
    
if __name__ == "__main__":
    main()    