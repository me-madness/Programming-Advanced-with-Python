from typing import Dict
# from __future__ import annotations  - this not go correct in Judje system, i can used in my projects

class Shop:
    def __init__(self, name: str, type_shop: str, capacity: int) -> None:
        self.name = name
        self.type_shop = type_shop
        self.capacity = capacity
        self.items: Dict[str: int] = {}
        
    
    @classmethod    
    def small_shop(cls, name: str, type_shop: str) -> str: # Here is possible to write the name of class "Shop" not "str"
        pass
    
    
    @classmethod
    def add_items(cls, item_name: str) -> str:
        pass
    
    
    @classmethod
    def remove_item(cls, item_name: str, amount: int) -> None:
        return f"{amount} {item_name} removed from the shop"
    return f"Cannot remove {amount} {item_name}"
    
    
    def __repr__(self) -> str:
       return f"{shop_name} of type {shop_type} with capacity {shop_capacity}"    