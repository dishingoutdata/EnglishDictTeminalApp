#!/usr/bin/env python
# coding: utf-8

# In[73]:


import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("Enter a word: ")

def translate(word):
    
    word = word.lower()
    
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data: 
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0:
        answer = input("Did you mean {} instead? Enter Y or N: ".format(get_close_matches(word, data.keys())[0]))
        if answer.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif answer.lower() == 'n':
            return "The word was not found. Please check it and try again."
        else:
            return "We didn't understand your entry."
    else:
        return "The word you entered doesn't exist."

output = (translate(word))

if type(output) == list:
    for definition in output:
        print('\n' + definition)
        
else:
    print(output)



# In[ ]:





# In[ ]:




