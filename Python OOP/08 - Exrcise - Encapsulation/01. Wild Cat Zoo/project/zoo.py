# from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
      self.name = name
      self.__budget = budget
      self.__animal_capacity = animal_capacity
      self.__workers_capacity = workers_capacity
      self.animals: list[Animal] = []
      self.workers: list[Worker] = []
      
      
    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append()(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return f"Not enough budget"
        return "Not enough space for animal"
    
    
    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    
    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"
    
    
    def pay_workers(self) -> str:
        money_to_pay = sum([w.salary for w in self.workers])
        
        if money_to_pay <= self.__budget:
            self.__budget -= money_to_pay
            return f"You payed your workers. They are happy. Budget left: {left_budget}"
        return f"You have no budget to pay your workers. They are unhappy"
    
    
    def tend_animals(self) -> str:
        money_to_feed_animals = sum([a.money_for_care for a in self.animals])
        
        if money_to_feed_animals <= self.__budget:
            self.__budget -= money_to_feed_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."
    
    
    def profit(self, amount: int):
        pass
    
    
    def animals_status(self):
        pass
    
    
    def __repr__(self) -> str:
        return f"You have {total_animals_count} animals
                    {amount_of_lions} Lions:{lion1} 
                    {lionN}
                    {amount_of_tigers} Tigers:
                    {tiger1}
                    {tigerN}
                    {amount_of_cheetahs} Cheetahs:
                    {cheetah1}
                    {cheetahN}"


print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())