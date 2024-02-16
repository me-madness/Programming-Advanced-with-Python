from collections import deque

worms = [int(el) for el in input().split()]
holes = deque([int(el) for el in input().split()])

while worms and holes:
    current_worm = worms[-1]
    current_hole = holes[0]
    
    if current_worm == current_hole:
        worms.pop()
        holes.popleft()
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()    