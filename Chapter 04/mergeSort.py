import math

def merging(left, right):
    newcabinet = []
    while (min(len(left), len(right)) > 0):
        if left[0] > right[0]:
            to_insert = right.pop(0)
            newcabinet.append(to_insert)
        elif left[0] <= right[0]:
            to_insert = left.pop(0)
            newcabinet.append(to_insert)

    if (len(left) > 0):
        for i in left:
            newcabinet.append(i)

    if (len(right) > 0):
        for i in right:
            newcabinet.append(i)

    return newcabinet


def mergesort_two_elements(cabinet):
    newcabinet = []
    if (len(cabinet) == 1):
        newcabinet = cabinet
    else:
        left = cabinet[:math.floor(len(cabinet)/2)]
        right = cabinet[math.floor(len(cabinet)/2):]
        newcabinet = merging(left, right)
    return newcabinet


def mergesort_four_elements(cabinet):
    newcabinet = []
    if (len(cabinet) == 1):
        newcabinet = cabinet
    else:
        left = mergesort_two_elements(cabinet[:math.floor(len(cabinet)/2)])
        right = mergesort_two_elements(cabinet[math.floor(len(cabinet)/2):])
        newcabinet = merging(left, right)
    return newcabinet


def mergesort(cabinet):
    newcabinet = []
    if (len(cabinet) == 1):
        newcabinet = cabinet
    else:
        left = mergesort(cabinet[:math.floor(len(cabinet)/2)])
        right = mergesort(cabinet[math.floor(len(cabinet)/2):])
        newcabinet = merging(left, right)
    return newcabinet


cabinet = [4,1,3,2,6,3,18,2,9,7,3,1,2.5,-9]
newcabinet = mergesort(cabinet)
print(newcabinet)