import sys

def parse(input_str):
    return [x.split("-") for line in input_str.strip().split('\n') for x in line.split(",")]

""" If sequence repeats twice in a row, it's invalid """
def invalid(num):
    s = str(num)
    return s[:len(s)//2] == s[len(s)//2:]  

""" If sequence repeats any number at least twice, it's invalid """
def invalid2(num):
    s = str(num)
    for i in range(1, len(s)//2 + 1):
        tot, res = divmod(len(s), i)
        if res == 0 and s[:i] * tot == s:
            return True
    return False

def part1(data):
    sum = 0
    for pair in data:
        start, end = pair
        for i in range(int(start), int(end)+1):
            if invalid(i):
                sum += i
    return sum

def part2(data):
    sum = 0
    for pair in data:
        start, end = pair
        for i in range(int(start), int(end)+1):
            if invalid2(i):
                sum += i
    return sum
if __name__ == "__main__":
    # Reads from a file named 'input.txt' in the same directory
    with open("inputs/day02.txt") as f:
        data = parse(f.read())
        
    with open("day02/test.txt") as f:
        test_data = parse(f.read())

    print(test_data)
    print(f"Part 1: {part1(test_data)}")
    print(f"Part 2: {part2(test_data)}")
    
    print(data)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")