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

rangeMin = 235741
rangeMax = 706948
matchedInputs = []
validInputs = []

for userInput in range(rangeMin, rangeMax) :
    input = [userInput]
    output = list(map(int, str(input[0])))
    #print(output)
    
    index = 0
    isTrue = True
    for singular in output :
        if index == 0 :
            #print(isTrue)
            index += 1 
        elif singular >= output[index - 1] :
            isTrue = True
            #print(isTrue)
            index += 1                
        else :
            isTrue = False
            #print(isTrue)
            break
        
    if isTrue == True :
        #print(userInput)
        matchedInputs.append(userInput)
    else :
        continue

for num in matchedInputs :
    input = [num]
    output = list(map(int, str(input[0])))
    
    index = 0
    count = 0
    isTrue = False
    for singular in output :
        if singular == output[index - 1] and count is not 2:
            count += 1
            isTrue = True
        else :
            isTrue = False
            continue
    
    if isTrue == True :
        #print(userInput)
        validInputs.append(num)
    else :
        continue
        

print(len(validInputs))
print(validInputs)