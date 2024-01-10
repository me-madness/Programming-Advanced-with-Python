# First from me

new_string = str(input())
reverse_string = reversed(new_string)
print(" ".join(reverse_string))

# Second task from the lecture

text = input()
print(text[::-1])

# Third task from the lecture

text = list(input())
while text:
    print(text.pop(), end="")

# Four task from the lecture

text = list(input())
stack = []

for i in range(len(text)):
    stack.append(text.pop())
    
print("".join(stack))    