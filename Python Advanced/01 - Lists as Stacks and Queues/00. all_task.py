# 01. Reverse String

# reverse_string = input()
# new_string_reversed = reversed(reverse_string)
# print(''.join(new_string_reversed))

# 02. Matching Parentheses

text = input()
parentheses = []

for i in range(len(text)):
    if text[i] == "(":
        parentheses.append(i)
    elif text[i] == ")":
        start_index = parentheses.pop()
        print(text[start_index:i + 1])
        
# 03. Supermarket




# 04. Water Dispenser




# 05. Hot Potato



