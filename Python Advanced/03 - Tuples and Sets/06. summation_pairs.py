# First task from the lecture

# First way from SOftUni

numbers = list(map(int, input().split()))
target = int(input())

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"{numbers[i] + {numbers[j]} = {target}}")

for i in range(len(numbers)):
    if numbers[i] == "":
        continue
    for j in range(i + 1, len(numbers)):
        if numbers[j] == "":
            continue
        if numbers[i] + numbers[j] == target:
            print(f"{numbers[i] + {numbers[j]} = {target}}")
            numbers[i] = ""
            numbers[j] = ""
            break
 
# Second way from SoftUni

numbers = list(map(int, input().split()))
target = int(input())

targets = set()
values_map = {}

for value in numbers:
    resulting_numbers = target - value
    targets.add(resulting_numbers)
    values_map[resulting_numbers] = value    

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f"{pair} + {value} = {target}")
    else:
        resulting_numbers = target - value
        targets.add(resulting_numbers)
        values_map[resulting_numbers] = value    

# Third way from softUni

import time

numbers = list(map(int, input().split()))
target = int(input())

start = time.time()
targets = set()
values_map = {}
for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f"{pair} + {value} = {target}")
    else:
        resulting_numbers = target - value
        targets.add(resulting_numbers)
        values_map[resulting_numbers] = value 
end = time.time()
print(f"Time range: {end-start}")        
            
# Second task from me