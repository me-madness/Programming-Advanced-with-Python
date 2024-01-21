# First task from the lecture

numbers = list(map(int, input().split()))
target = int(input())

# First way from SOftUni

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





            
# Second task from me

