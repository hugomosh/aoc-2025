# templates/template.py
import sys


def parse(input_str):
    return [line for line in input_str.strip().split("\n")]


def find_battery_simple(line, size):
    i = 0
    max_joltage = 0
    while i < len(line) - size + 1:
        j = i + 1
        while j < len(line):
            # print(f"{i},{j} Comparing {line[i]}{line[j]} to {max_joltage}")
            max_joltage = max(max_joltage, int(f"{line[i]}{line[j]}"))
            if int(line[j]) * 10 > max_joltage:
                # print(f"Breaking at j={j} with {line[j]}")
                i = j - 1
                break
            j += 1
        i += 1
    return max_joltage


""" Find the maximum joltage by picking N (size) digits, order preserved, from the line that maximize the resulting number."""


def find_battery_f(line, size):
    max_joltage_string = line[:size]
    max_joltage = int(max_joltage_string)
    i = 1
    while i < len(line):
        j = min(i - 1, size - 1)
        # replacing line[i] is_bigger than the current joltage at position j
        # there is enough space to the right to fill the rest of the joltage size
        # has to compare only to the last candidate position
        last_candidate = -1
        #print(f"{max_joltage_string}, At i={i}, j={j},  comparing {line[i]} to {max_joltage_string[j]} {line[i] >= max_joltage_string[j]} {size-j-1 }")
        while j >= 0 :
            if line[i] > max_joltage_string[j] and len(line) - i > size - j - 1:
                last_candidate = j
            j -= 1

        if last_candidate >= 0:
            # we can replace at last_candidate
            #print(f"Replacing at {last_candidate} with {line[i]} from {max_joltage_string}")
            max_joltage_string = (
                max_joltage_string[:last_candidate]
                + line[i : i + size - last_candidate]
            )
            #print(f"New joltage string: {max_joltage_string}")
            max_joltage = int(max_joltage_string)
            if  i + size - last_candidate ==  len(line) :
                return max_joltage
        i += 1

    return max_joltage

def find_battery(line,size):
    n = len(line)
    k = n - size # number of digits to remove 
    
    joltage = [] 
    for d in line:
        while len(joltage) > 0 and joltage[-1] < d and k > 0:
            joltage.pop()
            k -= 1
        joltage.append(d)
    return int("".join(joltage[:size]))
    
def find_battery_same_string(line, size):
    i=0
    while i < size:
        j = i+1
        print(f"{line} At i={i}, j={j}, comparing {line[i]} to {line[j]}")

            

        
            
def part1(data):
    sum = 0
    for line in data:
        sum += find_battery(line, 2)
        #print(f"Line: {line} => Max joltage: {find_battery(line,2)}")
    return sum


def part2(data):
    sum = 0
    for line in data:
        sum += find_battery(line, 12)
        #print(f"Line: {line} => Max joltage: {find_battery(line,12)}")
    return sum


def run_tests():
    with open("day03/test.txt") as f:
        test_data = parse(f.read())

    print(test_data)
    print(f"Part 1: {part1(test_data)}")
    print(f"Part 2: {part2(test_data)}")


if __name__ == "__main__":

    run_tests()
      
    # Reads from a file named 'input.txt' in the same directory
    with open("inputs/day03.txt") as f:
        data = parse(f.read())
        


    #print(data)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}") 

    for line in data:
        if find_battery(line,12) != find_battery_f(line,12):
            print(f"Line: {line} => Max joltage: {find_battery(line,12)} != {find_battery_f(line,12)}")
    
    line = "963127698647544464546543332"
    print(f"Line: {line} => Max joltage: {find_battery(line,4)} != {find_battery_f(line,4)}")

