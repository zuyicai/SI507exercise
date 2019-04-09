import random,json


def num_vowels(string):
    count =0
    vowels = ['a','e','i','o','u']
    # given the vowels
    for i in range((len(string))):
        if string[i].lower in vowels:
            count +=1
    return count
    # return the number of vowels in the string
