# First task from the lecture

numbers = tuple([float(el) for el in input().split()])

same_values = {}

for num in numbers:
    if num not in same_values:
        same_values[num] = numbers.count(num)
        
for number, occ in same_values.items():
    print(f"{number} - {occ} times")       
     
# Second way from the SoftUni

numbers = tuple(map(float, input().split()))

nums_and_occurances = {}

for num in numbers:
    if num not in nums_and_occurances:
        nums_and_occurances[num] += 1
    nums_and_occurances[num] += 1
    
[print(f"{key} - {value} times") for key, value in nums_and_occurances.items()]

# Second task from me

