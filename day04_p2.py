# --- Part Two ---
# An Elf just remembered one more important detail: the two adjacent 
# matching digits are not part of a larger group of matching digits.

# Given this additional criterion, but still ignoring the range rule, 
# the following are now true:

# - 112233 meets these criteria because the digits never decrease and 
#   all repeated digits are exactly two digits long.
# - 123444 no longer meets the criteria (the repeated 44 is part of a 
#   larger group of 444).
# - 111122 meets the criteria (even though 1 is repeated more than twice, 
#   it still contains a double 22).
# 
# How many different passwords within the range given in your puzzle 
# input meet all of the criteria?

# Your puzzle input is still 235741-706948.

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
            if 2 in Counter(output).values() :
                validInputs.append(output)
        
print(len(validInputs))
print(validInputs)