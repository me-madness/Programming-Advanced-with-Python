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
    
    
    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"
    
    
    def __repr__(self) -> str:
        return f"Account({self.owner}, {self.amount})"
    
    
    def __len__(self):
        return len(self._transaction)
    
    
    def __getItem__(self, idx: int):
        return self._transaction[idx]
    
    
    def __reversed__(self):
        return reversed(self._transaction)
    
    
    def __gt__(self, other):
        return self.balance > other.balance
    
    
    def __ge__(self, other):
        return self.balance >= other.balance
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    
    def __add_(self, other):
        new_account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_account._transaction = self._transaction + other._transaction
        
        return new_account
    
    
acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)    