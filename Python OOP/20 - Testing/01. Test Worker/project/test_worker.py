from unittest import TestCase, main
from project.worker import Worker


class TestWorker(TestCase):
    
    def setUp(self):        # runs before each test case
        self.worker = Worker("TestGuy", 25_000, 100)


    def test_correct_init(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(25_000, self.worker.salary)
        self.assertEqual(100, self.worker.name)
        self.assertEqual(0, self.worker.money)


if __name__ == "__main__":
    main()