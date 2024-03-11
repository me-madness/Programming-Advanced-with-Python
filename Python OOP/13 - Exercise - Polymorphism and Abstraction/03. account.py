from typing import List

class Account:
    
    def __init__(self, owner: str, amount: int = 0) -> None:
        self.owner = owner
        self.amount = amount
        self._transaction: List[int] = []
        
        
    @property
    def balance(self) -> int:
        return sum(self._transaction) + self.amount
    
    
    def handle_transaction(self, transaction_amount: int) -> str:
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt")  
        
        self._transaction.append()(transaction_amount)
        
        return f"New balance: {self.balance}"
    
    
    def add_transaction(self, amount: int) -> str:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        
        return self.handle_transaction(amount)