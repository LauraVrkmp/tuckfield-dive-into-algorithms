import math

def continuedFraction(x, y, length_tolerance):
    output = []
    big = max(x, y)
    small = min(x, y)
    while small > 0 and len(output) < length_tolerance:
        quotient = math.floor(big/small)
        output.append(quotient)
        new_small = big % small
        big = small
        small = new_small
    return output


def get_number(continuedFraction):
    index = -1
    number = continuedFraction[index]

    while abs(index) < len(continuedFraction):
        next = continuedFraction[index - 1]
        number = 1/number + next
        index -= 1
    return number


def continuedfractionDecimal(x, error_tolerance, length_tolerance):
    output = []
    first_tem = int(x)
    leftover = x - int(x)
    output.append(first_tem)
    error = leftover
    while error > error_tolerance and len(output) < length_tolerance:
        next_term = math.floor(1 / leftover)
        leftover = 1 / leftover - next_term
        output.append(next_term)
        error = abs(get_number(output) - x)
    return output

print(continuedFraction(105, 33, 10))
print(get_number([3, 5, 2]))
print(continuedfractionDecimal(1.4142135623730951, 0.00001, 100))
