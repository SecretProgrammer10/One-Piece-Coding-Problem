# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:42:23 2020

@author: The Wonder Land

"""

import random
import string

max_puzzle_length = int(1e4)
max_pattern_length = 8

def test_case_generator():
    puzzle_length = random.randrange(20, max_puzzle_length)
    puzzle_letters = string.ascii_lowercase
    pattern_length = random.randrange(2, max_pattern_length)
    pattern_letters = string.ascii_letters
    pattern = ''.join(random.choice(pattern_letters) for _ in range(pattern_length))
    pattern_lower = pattern.lower()
    length = 0
    pattern_occurrence = 0
    #pattern_chars = list(pattern_lower[i] for i in range(pattern_length))
    rem = int(puzzle_length)
    puzzle = ""
    for i in range(pattern_length):
        puzzle_letters = puzzle_letters.replace(pattern_lower[i], '')
    while rem > 0:
        random_length = random.randint(1,int(rem/2))
        for _ in range(random_length):
            puzzle = "".join((puzzle,random.choice(puzzle_letters)))
        puzzle = "".join((puzzle, pattern_lower))
        pattern_occurrence += 1
        length = len(puzzle)
        rem -= length
    
    print(puzzle)
    print()
    print(pattern)
    print()
    print(pattern_occurrence)
    print()

if __name__ == '__main__':
    print("Enter no. of test cases required:")
    n = int(input())
    i = n
    while(n!=0):
        print("Test Case", i-n+1,":")
        test_case_generator()
        n -= 1
    

