from unittest import TestCase, main
from hashtable import HashTable

class TestHashTable(TestCase):
    
    def setUp(self):
        self.h = HashTable()
    
    
    def test_init(self):
        self.assertEqual(self.h_Hashtable__keys, [None, None, None, None])
        self.assertEqual(self.h_Hashtable__values, [None, None, None, None])
        self.assertEqual(self.h_Hashtable__length, 4)
    
    
if __name__ == "__main__":
    main()    