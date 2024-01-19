# First task from the lecture

num = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(num)]
primary_sum, second_sum = 0, 0

for i in range(num):
    primary_sum +=matrix[i][i]
    second_sum += matrix[i][num - i - 1]

print(abs(primary_sum - second_sum))

# Second way from the lecture

n = int(input())
primary_sum, second_sum = 0, 0

for i in range(n):
    line = [int(el) for el in input().split()]
    primary_sum +=line[i][i]
    second_sum += line[i][num - i - 1]

print(abs(primary_sum - second_sum))



# Second task from me

