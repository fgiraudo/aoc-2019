import math
import os
import copy

#Change Python working directory to source file path
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def main():
    count = 0

    print(is_valid(112233))
    print(is_valid(123444))
    print(is_valid(112223))

    for password in range(256310, 732737):
        if is_valid(password):
            count += 1
    
    print(count)

def is_valid(password):
    digits = [int(d) for d in str(password)]

    last_digit = digits.pop(0)
    has_adjacent = False
    adjacent_digit = None
    invalid_adjacent = None

    has_valid_adjacent = False
    
    for digit in digits:
        if digit < last_digit:
            return False

        if digit > last_digit and has_adjacent:
            has_valid_adjacent = True

        if digit == last_digit:
            if (has_adjacent and adjacent_digit == digit) or invalid_adjacent == digit:
                adjacent_digit = None
                invalid_adjacent = digit
                has_adjacent = False
            else:
                adjacent_digit = digit
                has_adjacent = True
        
        last_digit = digit
        
    return has_adjacent or has_valid_adjacent

main()