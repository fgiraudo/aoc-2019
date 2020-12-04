import math
import os

#Change Python working directory to source file path
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def fuel_required(mass):
    return max(0, math.floor(mass / 3) - 2)

modules = []

with open("../Inputs/input-day1.txt") as inputFile:
    modules = inputFile.read().splitlines()

    sum = 0

    for module in modules:
        fuel = fuel_required(int(module))

        extra_fuel = fuel_required(fuel)

        while(extra_fuel > 0):
            fuel += extra_fuel
            extra_fuel = fuel_required(extra_fuel)

        sum += fuel

    print(sum)

