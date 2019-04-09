import random

def num_vowels(string):
    count =0
    vowels = ['a','e','i','o','u']
    for i in range((len(string))):
        if string[i].lower in vowels:
            count +=1
    return count
