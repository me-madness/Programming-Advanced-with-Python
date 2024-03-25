from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    
    def setUp(self):
        self.mammal = Mammal("some name", "some type", "some sound")

    
    def test_correct_init(self):
        self.assertEqual("some name", self.mammal.name)
        self.assertEqual("some type", self.mammal.type)
        self.assertEqual("some sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom__)





if __name__ == "__main__":
    main()