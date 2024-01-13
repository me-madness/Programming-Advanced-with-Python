# First task from the lecture

from collections import deque

numbers = deque(input().split())
numbers.reverse()
print(*numbers)

# Second way from the lecture

numbers = deque(input().split())

for _ in range(len(numbers)):
    print(numbers.pop(), end=" ")

# Second task from me

