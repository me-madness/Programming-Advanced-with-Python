from unittest import TestCase, main
from cat import Cat

class TestCat(TestCase):
    
    def setUp(self):
        self.cat = Cat("Pancho")


    def test_correct_init(self):
        self.assertEqual("Pancho", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)


    def test_feed_cat_makes_cat_sleepy_and_not_hungry_expect_size_increase_by_1(self):
        



if __name__ == "__main__":
    main()