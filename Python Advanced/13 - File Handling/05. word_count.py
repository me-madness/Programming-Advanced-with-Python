# First task from the lecture

import os
import re

words_path = os.path.join("resources", "words.txt")
text_path = os.path.join("resources", "input.txt")

with open(words_path) as file:
    searched_words_as_text = file.read()
    searched_words = [word.lower() for word in searched_words_as_text.split()]
    
    
with open(text_path) as file:
    content = file.read().lower()
    
words_count = {}

for searched_word in searched_words:
    regex = re.compile(rf"\b{searched_word}")
        
"output.txt"


# Second task from me



