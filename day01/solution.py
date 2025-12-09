# templates/template.py
import sys
from operator import sub, add

def parse(input_str):
    return [line for line in input_str.strip().split('\n')]

def part1b(data):
    count = 0
    dial = 50

    for line in data:
        direction = 1 if line[0] == "R" else -1
        amount = int(line[1:])
        dial += (amount * direction) 
        dial = dial % 100
        #print (f"{dial} {direction} {line} {amount} {amount * direction}" )
        if dial == 0:
            count+=1
    return count

def part1(data):
    count = 0
    dial = 50

    for line in data:
        direction = 1 if line[0] == "R" else -1
        amount = int(line[1:])
        wraps, steps = divmod(amount, 100)
        new_dial = dial + (steps * direction) 
        dial = new_dial %100
        if dial == 0:
           count+=1
    return count


def part2(data):
    count = 0
    dial = 50

    for line in data:
        direction = 1 if line[0] == "R" else -1
        amount = int(line[1:])
        wraps, steps = divmod(amount, 100)
        new_dial = dial + (steps * direction) 
        count += wraps
        # we don't count leaving 0 and we pass 0 an extra time if we are not in the first range (0,100)
        if dial != 0 and not ( 0 < new_dial < 100 ):
            count+=1
        dial = new_dial %100

    return count


def part2_brute(data):
    count = 0
    dial = 50

    for line in data:
        direction = 1 if line[0] == "R" else -1
        amount = int(line[1:])
        new_dial = dial + (amount * direction) 
        #print (f"{dial} {direction} {line} {amount} {amount * direction}" )
        path = range(dial +1,new_dial+  1) if direction == 1 else range (new_dial, dial)
        for x in path:
            if x %100 == 0:
                count +=1
        dial = new_dial % 100

    return count



if __name__ == "__main__":
    # Reads from a file named 'input.txt' in the same directory
    with open("inputs/day01.txt") as f:
        data = parse(f.read())

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2_clean(data)}")