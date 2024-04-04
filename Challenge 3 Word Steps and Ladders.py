#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:23:57 2024

@author: maggielyon
"""
#importing the words list
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

#step word returns true if the word is a target word 
def step_word(word, target_word):
    #we only want to check words that are the correct length (word + 1)
    # to increase the efficiency of this function
    if len(word) != len(target_word) - 1:
        return False
    #create a 2d array with each character in the word and a corresponding flag
    letters = [[letter, False] for letter in word]

    # Check if each letter in target_word is in word 
    for char in target_word:
        #letters is a list [letter, flag]
        for letter in letters:
            if letter[0] == char and letter[1] == False:
                letter[1] = True
                # Exit the loop once the letter is found to increase efficiency
                break  
    #if all flags are set to true, the target word is a step word
    return all(flag for _, flag in letters)


def allsteps(word):
    #adds the target word in words if step_word is true
    return [target for target in words if step_word(word, target)]

# Test cases
print(allsteps("APPLE"))
print(allsteps("UC"))
print(allsteps("BEARCAT"))

# To speed up my solution, I used a break statement in the step_word loop so that
#once a letter is found, we do not need to keep iterating through each word. 
#in addition, the loop only checks words which are the correct length, greatly
#narrowing down the options and increasing efficiency as we don't need to iterate 
#through every letter of every word, just a few letters until it is found in words
#that are possible. 