# First task from the lecture

occurrences = {}

for symbol in input():
    occurrences[symbol] = occurrences.get(symbol, 0) + 1


for letter, times in sorted(occurrences.items()):
    print(f"{symbol}: {times} time/s")
    
# Second way from the lecture

text = input()

for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")
   
# Second task from me

