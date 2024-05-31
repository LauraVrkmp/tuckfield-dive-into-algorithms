import math

nested = [2, 1]

def nestedRadical(nested, length_tolerance):
    x = math.sqrt(nested[0] + nested[1])
    i = 1
    while i <= length_tolerance:
        print(x)
        x = math.sqrt(nested[0] + (nested[1]) * x)
        i += 1
    return x

print(nestedRadical(nested, 10))