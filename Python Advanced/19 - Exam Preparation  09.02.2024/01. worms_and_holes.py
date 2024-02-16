from collections import deque

worms = [int(el) for el in input().split()]
holes = deque([int(el) for el in input().split()])

all_worms_count = len(worms)
count = 0

while worms and holes:
    current_worm = worms[-1]
    current_hole = holes[0]
    
    if current_worm == current_hole:
        worms.pop()
        holes.popleft()
        count += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()  


if count:
    print(f"Matches: {count}")              
else:
    print(f"There are no matches.")              
                            
if not worms and count == all_worms_count:
    print(f"Every worm found a suitable hole!")              
elif not worms and count < all_worms_count:                  
    print(f"Worms left: none")              
else:
    print(f"Worms left: {', '.join([str(el) for el in worms])}")              
                        
if not holes:
    print(f"Holes left: none")              
else:                
    print(f"Worms left: {', '.join([str(el) for el in holes])}")              