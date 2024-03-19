from abc import ABC, abstractmethod

@abstractmethod
class Person(ABC):
    def say_hi(self):
        pass
    
    
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi


print(hello_function)    