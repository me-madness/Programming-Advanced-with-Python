# First task from the lecture

from collections import deque

names = deque(input()).split()
n_toss = int(input()) -1

while len(names) > 1:
    names.rotate(-n_toss)
    removed_kid = names.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {removed_kid}")




# Second task from me