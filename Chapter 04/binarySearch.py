import math

sortedCabinet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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

print(binarySearch(sortedCabinet, 8))
