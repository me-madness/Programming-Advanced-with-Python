# 01. Reverse String

# reverse_string = input()
# new_string_reversed = reversed(reverse_string)
# print(''.join(new_string_reversed))

# 02. Matching Parentheses

# text = input()
# parentheses = []

# for i in range(len(text)):
#     if text[i] == "(":
#         parentheses.append(i)
#     elif text[i] == ")":
#         start_index = parentheses.pop()
#         print(text[start_index:i + 1])
        
# 03. Supermarket

# from collections import deque

# supermarket = deque()

# while True:
#     command = input()
#     if command == "Paid":
#         while len(supermarket):
#             print(supermarket.popleft())
#     elif command == "End":
#         print(f"{len(supermarket)} people remaining.")
#         break
#     else:
#         supermarket.append(command)        

# 04. Water Dispenser

from collections import deque

water_dispenser = deque()
water_quantity = int(input())
name = input()
command = input()

while command != "End":
    if "refill" in command:
        pass
    else:
        liters = int(command)
        if liters <= water_quantity:
            water_quantity -= liters
            print(f"{water_dispenser.popleft()} got water")
        else:
            print(f"{water_dispenser.popleft()} must wait")
    command = input()   
print(f"{water_quantity} liters left")    

# 05. Hot Potato



