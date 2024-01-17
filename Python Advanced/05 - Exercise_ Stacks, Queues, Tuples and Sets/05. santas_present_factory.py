# First task from the lecture

from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[-1] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0
    
    if not magic_level:
        continue

    product = material * magic_level
    
    if presents.get(product):
        crafted.append()(presents[product])
    
print("The presents are crafted! Merry Christmas")
print("No presents this Christmas")
print(f"Materials left: {}, {}, {}")
print(f"Magic left: {}, {}, {}")
print(f"{}: {}")



# Second task from me

