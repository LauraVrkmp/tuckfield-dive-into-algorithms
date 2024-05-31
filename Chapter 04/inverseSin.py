import math

def binarySearch(sorted_cabinet, looking_for):
    guess = math.floor(len(sorted_cabinet) / 2)
    upperbound = len(sorted_cabinet)
    lowerbound = 0

    while (abs(sorted_cabinet[guess] - looking_for) > 0.0001):
        if (sorted_cabinet[guess] > looking_for):
            upperbound = guess
            guess = math.floor((guess + lowerbound) / 2)
        if (sorted_cabinet[guess] < looking_for):
            lowerbound = guess
            guess = math.floor((guess + upperbound) / 2)
    return guess


def inverse_sin(number):
    domain = [x * math.pi/10000 - math.pi / 2 for x in list(range(0, 10000))]
    the_range = [math.sin(x) for x in domain]
    result = domain[binarySearch(the_range, number)]
    return result


print(inverse_sin(0.9))