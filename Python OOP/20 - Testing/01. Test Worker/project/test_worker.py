from unittest import TestCase, main
from worker import Worker


class TestWorker(TestCase):
    
    def setUp(self):        # runs before each test case
        self.worker = Worker("TestGuy", 25_000, 100)


    def test_correct_init(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(25_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)


    def test_work_when_worker_has_energy_expect_money_increase_and_energy_decrease(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2
    
        self.worker.work()
        self.worker.work()
        
        
        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)
        
        
if __name__ == "__main__":
    main()