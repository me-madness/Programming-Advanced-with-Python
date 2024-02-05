# First task from the lecture

import os
import re

words_path = os.path.join("resources", "words.txt")
text_path = os.path.join("resources", "input.txt")
output_file_path = os.path.join("resources", "output.txt")

with open(words_path) as file:
    searched_words_as_text = file.read()
    searched_words = [word.lower() for word in searched_words_as_text.split()]
    
    
with open(text_path) as file:
    content = file.read().lower()
    
words_count = {}

for searched_word in searched_words:
    regex = re.compile(rf"\b{searched_word}")
    results = re.findall(regex, content)
    words_count[searched_word] = len(results)         #result.count(searched_word)
    
sorted_words_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])    
 
with open(output_file_path) as file:
    for word, count in sorted_words_count:
        file.write(f"{word} - {count}\n ")            


# Second task from me



