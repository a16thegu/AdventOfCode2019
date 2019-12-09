# --- Day 4: Secure Container ---
# You arrive at the Venus fuel depot only to discover it's protected by a password. The 
# Elves had written the password on a sticky note, but someone threw it out.

# However, they do remember a few key facts about the password:

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay 
# the same (like 111123 or 135679).
# Other than the range rule, the following are true:

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these 
# criteria?

# Your puzzle input is 235741-706948.

# Borrowed code from https://github.com/sswingle/advent-of-code/blob/master/day04.py
# To understand what to do and for me to change the logic in my code, to solve the 
# puzzle using my logic.

# from collections import Counter

# def check1(s):
#     return list(s) == sorted(s) and len(set(s)) < len(s) 

# def check2(s):
#     return list(s) == sorted(s) and 2 in Counter(s).values()

# print(sum(check1(str(x)) for x in range(235741, 706948)))
# print(sum(check2(str(x)) for x in range(235741, 706948)))

from collections import Counter

rangeMin = 235741
rangeMax = 706948
validInputs = []

for userInput in range(rangeMin, rangeMax) :
    input = [userInput]
    output = list(map(int, str(input[0])))
    #print(output)
    
    if output == sorted(output) :
        if len(set(output)) < len(output) :
            validInputs.append(output)
        
print(len(validInputs))
print(validInputs)