# templates/template.py
import sys

def parse(input_str):
    return [line for line in input_str.strip().split('\n')]

def part1(data):
    return "TODO"

def part2(data):
    return "TODO"

if __name__ == "__main__":
    # Reads from a file named 'input.txt' in the same directory
    with open("inputs/day01.txt") as f:
        data = parse(f.read())

    print(data)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")