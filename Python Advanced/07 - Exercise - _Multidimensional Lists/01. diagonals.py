# First task from the lecture

n = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(n)] # ["1, 2, 3, 4", "1, 2, 3"]
primary = [matrix[r][r] for r in range(n)]
second= [matrix[r][n - r - 1] for r in range(n)]



print(f"Primary diagonal: {}, {}, {}. Sum: {}")
print(f"Second diagonal: {}, {}, {}. Sum: {}")



# Second task from me

