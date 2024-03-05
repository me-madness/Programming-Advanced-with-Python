class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
      self.name = name
      self.__budget = budget
      self.__animal_capacity = animal_capacity
      self.__workers_capacity = workers_capacity
      self.animals = []
      self.workers = []
      
      
    def add_animal(self, animal:str, price: int) -> str:
        pass
    
    
    def hie_worker(self, worker: str) -> str:
        pass
    
    
    def fire_worker(self, worker_name: str) -> str:
        pass
    
    
    def pay_workers(self):
        return f"You payed your workers. They are happy. Budget left: {left_budget}"
        return f"You have no budget to pay your workers. They are unhappy"
    
    
    def tend_animals(self):
        return f"You tended all the animals. They are happy. Budget left: {left_budget}"
        return f"You have no budget to tend the animals. They are unhappy."
    
    
    def profit(self, amount: int):
        pass
    
    
    def animals_status(self):
        pass