import math
import os
import copy

#Change Python working directory to source file path
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def main():
    with open("../Inputs/input-day3.txt") as input_file:
        wires_path = parse_input(input_file)
        
        print(wires_path)

        intersections = find_intersections(wires_path)

        distance = None
        steps = None

        for point in intersections:
            if point == (0,0):
                continue
            
            manhattan_distance = abs(point[0]) + abs(point[1])

            if distance == None:
                distance = manhattan_distance
            else:
                distance = min(distance, manhattan_distance)

            min_steps = steps_to(point, wires_path[0]) + steps_to(point, wires_path[1])

            if steps == None:
                steps = min_steps
            else:
                steps = min(steps, min_steps)
            
        print(distance)
        print(steps)

def parse_input(input_file):
    paths = input_file.read().splitlines()

    result = []

    for path in paths:
        result.append(path.split(","))
    
    return result

def find_intersections(wires_path):
    return set(all_points(wires_path[0])) & set(all_points(wires_path[1]))

def all_points(path):
    result = [(0,0)]

    x = 0
    y = 0

    for segment in path:
        direction = segment[0]
        moves = int(segment[1:])

        for _ in range(moves):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            else:
                y -= 1

            result.append((x,y))
    
    return result

def steps_to(point, path):
    steps = 0

    x = 0
    y = 0

    for segment in path:
        direction = segment[0]
        moves = int(segment[1:])

        for _ in range(moves):
            steps += 1

            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            else:
                y -= 1
            
            if (x,y) == point:
                return steps
main()