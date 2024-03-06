from typing import Dict


class Shop:
    def __init__(self, name: str, type_shop: str, capacity: int):
        self.name = name
        self.type_shop = type_shop
        self.capacity = capacity
        self.items: Dict[str: int] = {}
        
        
    def small_shop(self, name: str, type: str):
        pass
    
    
    def add_items(self, item_name: str):
        pass
    
    
    def remove_item(self, item_name: str, amount: int):
        return f"{amount} {item_name} removed from the shop"
    return f"Cannot remove {amount} {item_name}"
    
    
    def __repr__(self) -> str:
       return f"{shop_name} of type {shop_type} with capacity {shop_capacity}"    