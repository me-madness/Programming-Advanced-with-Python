from collections import deque

money_in_pocket = [int(el) for el in input().split()]
prices_of_foods = deque([int(el) for el in input().split()])

food_count = 0

while money_in_pocket and prices_of_foods:
    current_money = money_in_pocket[-1]
    current_price = prices_of_foods[0]
    
    if current_money > current_price:
        rest_money = current_money - current_price
        money_in_pocket.pop()
        prices_of_foods.popleft()
        money_in_pocket[-1] += rest_money
        food_count +=1
    elif current_money == current_price:
        money_in_pocket.pop()
        prices_of_foods.popleft()
        food_count +=1
    else:
        money_in_pocket.pop()
        prices_of_foods.popleft()   
            
    
    
    
    
    
print(f"Gluttony of the day! Henry ate {food_count} foods.")    
print(f"Henry ate: {food_count} foods.")    
print(f"Henry ate: {food_count} food.")    
print(f"Henry remained hungry. He will try next weekend again.")    