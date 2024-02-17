from collections import deque

money_in_pocket = [int(el) for el in input().split()]
prices_of_foods = deque([int(el) for el in input().split()])

food_count = 0

while money_in_pocket and prices_of_foods:
    