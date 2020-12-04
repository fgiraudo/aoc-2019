import math
import os
import copy

#Change Python working directory to source file path
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def main():
    with open("../Inputs/input-day2.txt") as input_file:
        memory = parse_input(input_file)
        
        print(memory)
        print(noun_and_verb(memory))
        
def parse_input(input_file):
    string_input = input_file.read().strip().split(',')
    numeric_input = [int(string) for string in string_input]
    numeric_input[1] = 12
    numeric_input[2] = 2

    return numeric_input

def intcode(numeric_input):
    index = 0

    while numeric_input[index] != 99:
        if numeric_input[index] == 1:
            numeric_input[numeric_input[index + 3]] = numeric_input[numeric_input[index + 1]] + numeric_input[numeric_input[index + 2]]
        else:
            numeric_input[numeric_input[index + 3]] = numeric_input[numeric_input[index + 1]] * numeric_input[numeric_input[index + 2]]

        index += 4

    return numeric_input

def noun_and_verb(memory):
    for noun in range(100):
        for verb in range(100):
            numeric_input = copy.copy(memory)
            numeric_input[1] = noun
            numeric_input[2] = verb

            if intcode(numeric_input)[0] == 19690720:
                return 100 * noun + verb
    
    return 0

main()