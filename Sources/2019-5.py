import math
import os
import copy

#Change Python working directory to source file path
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def main():
    with open("../Inputs/input-day5.txt") as input_file:
        memory = parse_input(input_file)
        
        intcode(memory)
        
def parse_input(input_file):
    string_input = input_file.read().strip().split(',')
    numeric_input = [int(string) for string in string_input]
    
    return numeric_input

def intcode(numeric_input):
    index = 0

    while get_opcode(numeric_input[index]) != 99:
        instruction = digits_for(numeric_input[index])
        opcode = get_opcode(numeric_input[index])

        if opcode == 1:
            first_parameter = numeric_input[numeric_input[index + 1]] if instruction[2] == 0 else numeric_input[index + 1]
            second_parameter = numeric_input[numeric_input[index + 2]] if instruction[1] == 0 else numeric_input[index + 2]
            numeric_input[numeric_input[index + 3]] = first_parameter + second_parameter
            index += 4
        
        elif opcode == 2:
            first_parameter = numeric_input[numeric_input[index + 1]] if instruction[2] == 0 else numeric_input[index + 1]
            second_parameter = numeric_input[numeric_input[index + 2]] if instruction[1] == 0 else numeric_input[index + 2]
            numeric_input[numeric_input[index + 3]] = first_parameter * second_parameter
            index += 4
        
        elif opcode == 3:
            user_input = int(input("Please input a valid integer: "))
            numeric_input[numeric_input[index + 1]] = user_input
            index += 2
        
        elif opcode == 4:
            value = numeric_input[numeric_input[index + 1]] if instruction[2] == 0 else numeric_input[index + 1]
            print(value)
            index += 2

        elif opcode == 5:
            first_parameter = numeric_input[numeric_input[index + 1]] if instruction[2] == 0 else numeric_input[index + 1]
            second_parameter = numeric_input[numeric_input[index + 2]] if instruction[1] == 0 else numeric_input[index + 2]

            if first_parameter != 0:
                index = second_parameter
            else:
                index += 3
        
        elif opcode == 6:
            first_parameter = numeric_input[numeric_input[index + 1]] if instruction[2] == 0 else numeric_input[index + 1]
            second_parameter = numeric_input[numeric_input[index + 2]] if instruction[1] == 0 else numeric_input[index + 2]

            if first_parameter == 0:
                index = second_parameter
            else:
                index += 3

        elif opcode == 7:
            first_parameter = numeric_input[numeric_input[index + 1]] if instruction[2] == 0 else numeric_input[index + 1]
            second_parameter = numeric_input[numeric_input[index + 2]] if instruction[1] == 0 else numeric_input[index + 2]

            if first_parameter < second_parameter:
                numeric_input[numeric_input[index + 3]] = 1
            else: 
                numeric_input[numeric_input[index + 3]] = 0
            
            index += 4

        elif opcode == 8:
            first_parameter = numeric_input[numeric_input[index + 1]] if instruction[2] == 0 else numeric_input[index + 1]
            second_parameter = numeric_input[numeric_input[index + 2]] if instruction[1] == 0 else numeric_input[index + 2]
            
            if first_parameter == second_parameter:
                numeric_input[numeric_input[index + 3]] = 1
            else: 
                numeric_input[numeric_input[index + 3]] = 0

            index += 4

    return numeric_input

def get_opcode(instruction):
    digits = digits_for(instruction)

    return digits[3] * 10 + digits[4]


def digits_for(instruction):
    digits = [int(d) for d in str(instruction)]

    while len(digits) < 5:
        digits.insert(0,0)
    
    return digits


main()