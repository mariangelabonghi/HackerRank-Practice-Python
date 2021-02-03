#!/bin/python3

def countingValleys(steps, path):
    level = 0
    valleys = 0
    for step in path:
        new_level = level
        if step == 'U':
            level += 1
        else:
            level -= 1
        if level < 0 and new_level == 0:
            valleys += 1
    return valleys

if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(result)
